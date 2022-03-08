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
            return range(self.from_x, self.to_x - 1, -1)

    def y_range(self):
        if self.from_y < self.to_y:
            return range(self.from_y, self.to_y + 1)
        else:
            return range(self.from_y, self.to_y - 1, -1)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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


def add_diagonal_line(line, diagram):
    points = []
    current_point = 0
    y_range = list(line.y_range())
    x_range = list(line.x_range())
    while current_point < len(y_range):
        points.append(Point(x_range[current_point], y_range[current_point]))
        current_point += 1

    for point in points:
        diagram[point.y][point.x] += 1


def add_all_lines_to_diagram(lines, diagram):
    for line in lines:
        if line.is_vertical():
            add_vertical_line(line, diagram)
        elif line.is_horizontal():
            add_horizontal_line(line, diagram)
        else:
            add_diagonal_line(line, diagram)
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
    vent_lines = parse_input(vent_input)

    vent_diagram = initialize_vent_diagram(1000, 1000)

    add_all_lines_to_diagram(vent_lines, vent_diagram)

    print("Answer: " + str(calculate_number_of_hotspots(vent_diagram)))


main()
