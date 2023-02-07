def create_tree_grid(tree_input):
    grid_size = len(tree_input)
    grid = [[] for _ in range(grid_size)]
    for line in tree_input:
        for i in range(grid_size):
            grid[i].append(line[i])
    return grid


def is_visible(tree_grid, x, y):
    left_max = max([tree_grid[left_x][y] for left_x in range(x)])
    right_max = max([tree_grid[right_x][y] for right_x in range(x + 1, len(tree_grid))])
    up_max = max(tree_grid[x][:y])
    down_max = max(tree_grid[x][y + 1:])
    if any(tree_max < tree_grid[x][y] for tree_max in [left_max, right_max, up_max, down_max]):
        return True


def calculate_visible_trees(tree_grid):
    grid_size = len(tree_grid)
    visible_treees = grid_size * 4 - 4
    for x in range(1, grid_size - 1):
        for y in range(1, grid_size - 1):
            if is_visible(tree_grid, x, y):
                visible_treees += 1

    return visible_treees


def viewing_distance(tree_hight, tree_line):
    distance = 0
    for tree in tree_line:
        if tree < tree_hight:
            distance += 1
        else:
            distance += 1
            break
    return distance


def calculate_scenic_score(tree_grid, x, y):
    tree_hight = tree_grid[x][y]
    left = [tree_grid[left_x][y] for left_x in range(x)]
    right = [tree_grid[right_x][y] for right_x in range(x + 1, len(tree_grid))]
    up = tree_grid[x][:y]
    down = tree_grid[x][y + 1:]

    left_score = viewing_distance(tree_hight, list(reversed(left)))
    right_score = viewing_distance(tree_hight, right)
    up_score = viewing_distance(tree_hight, list(reversed(up)))
    down_score = viewing_distance(tree_hight, down)

    return left_score * right_score * up_score * down_score


def calculate_max_scenic_score(tree_grid):
    grid_size = len(tree_grid)
    max_scenic_score = 0
    for x in range(1, grid_size - 1):
        for y in range(1, grid_size - 1):
            current_scenic_score = calculate_scenic_score(tree_grid, x, y)
            if current_scenic_score > max_scenic_score:
                max_scenic_score = current_scenic_score

    return max_scenic_score


def main():
    tree_input = open('input').read().splitlines()
    tree_grid = create_tree_grid(tree_input)

    part1_answer = calculate_visible_trees(tree_grid)
    print("Answer part 1: {}".format(part1_answer))

    part2_answer = calculate_max_scenic_score(tree_grid)
    print("Answer part 2: {}".format(part2_answer))


main()
