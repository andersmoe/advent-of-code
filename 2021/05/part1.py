class Line:
    def __init__(self, from_x, from_y, to_x, to_y):
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y

    def is_vertical(self):
        return self.from_x == self.to_x

    def is_horizontal(self):
        return self.from_y == self.to_y

    def x_range(self):
        if self.from_x < self.to_x:
            return range(self.from_x, self.to_x + 1)
        else:
            return range(self.to_x, self.from_x + 1)

    def y_range(self):
        if self.from_y < self.to_y:
            return range(self.from_y, self.to_y + 1)
        else:
            return range(self.to_y, self.from_y + 1)


def initialize_vent_diagram(rows, columns):
    return [[0 for x in range(columns)] for i in range(rows)]


def parse_input(vent_input):
    vent_lines = [line.replace(" -> ", ",").split(",") for line in vent_input]
    lines = [Line(int(from_x), int(from_y), int(to_x), int(to_y)) for from_x, from_y, to_x, to_y in vent_lines]
    return lines


def add_horizontal_line(line, diagram):
    for x in line.x_range():
        diagram[line.from_y][x] += 1
    return


def add_vertical_line(line, diagram):
    for y in line.y_range():
        diagram[y][line.from_x] += 1
    return


def add_all_lines_to_diagram(lines, diagram):
    for line in lines:
        if line.is_vertical():
            add_vertical_line(line, diagram)
        elif line.is_horizontal():
            add_horizontal_line(line, diagram)
    return


def calculate_number_of_hotspots(diagram):
    hotspots = 0
    for y in diagram:
        for x in y:
            if x > 1:
                hotspots += 1
    return hotspots


def main():
    vent_input = open('input.txt').read().splitlines()

    vent_diagram = initialize_vent_diagram(1000, 1000)
    add_all_lines_to_diagram(parse_input(vent_input), vent_diagram)

    print("Answer: " + str(calculate_number_of_hotspots(vent_diagram)))


main()
