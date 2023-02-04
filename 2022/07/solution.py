class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirs = []
        self.size = 0

    def add_size(self, size):
        self.size += size

    def add_subdir(self, subdir):
        self.subdirs.append(subdir)

    def get_subdir(self, name):
        for subdir in self.subdirs:
            if subdir.name == name:
                return subdir
        return None

    def folder_size(self):
        total_size = self.size
        for subdir in self.subdirs:
            total_size += subdir.folder_size()
        return total_size

    def get_all_dirs(self):
        all_dirs = [self]
        for subdir in self.subdirs:
            all_dirs += subdir.get_all_dirs()
        return all_dirs


def create_filesystem(terminal_input):
    filesystem = Dir("/", None)
    current_dir = filesystem
    for line in terminal_input[1:]:
        first, *middle, last = line.split(" ")
        if first == "$":
            if middle and middle[0] == "cd":
                if last == "..":
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.get_subdir(last)
        elif first == "dir":
            dirname = list(line.split(" "))[-1]
            current_dir.add_subdir(Dir(dirname, current_dir))
        else:
            current_dir.add_size(int(first))

    return filesystem


def total_size_of_dirs_under_100000(filesystem):
    total_size = 0
    all_dirs = filesystem.get_all_dirs()
    for current_dir in all_dirs:
        folder_size = current_dir.folder_size()
        if folder_size <= 100000:
            total_size += folder_size
    return total_size


def size_of_directory_to_delete(filesystem):
    space_needed = 30000000 - (70000000 - filesystem.folder_size())
    delete_size = filesystem.folder_size()
    for current_dir in filesystem.get_all_dirs():
        folder_size = current_dir.folder_size()
        if space_needed <= folder_size < delete_size:
            delete_size = folder_size
    return delete_size


def main():
    terminal_input = open('input').read().splitlines()

    filesystem = create_filesystem(terminal_input)

    part1_answer = total_size_of_dirs_under_100000(filesystem)
    print("Answer part 1: {}".format(part1_answer))

    part2_answer = size_of_directory_to_delete(filesystem)
    print("Answer part 2: {}".format(part2_answer))


main()
