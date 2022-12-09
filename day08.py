example = """30373
25512
65332
33549
35390
"""


def parse(data):
    grid = {}
    lines = data.strip().splitlines()

    for row, trees in enumerate(lines):
        for column, tree in enumerate(trees):
            grid[(column, row)] = int(tree)

    return grid, len(lines[0]), len(lines)


def day8a(data):
    grid, max_x, max_y = parse(data)

    visible = set()

    # l to r
    for y in range(max_y):
        vis_h = -1
        for x in range(max_x):
            h = grid.get((x, y))
            if h > vis_h:
                visible.add((x, y, h))
                vis_h = h

    # r to l
    for y in range(max_y):
        vis_h = -1
        for x in reversed(range(max_x)):
            h = grid.get((x, y))
            if h > vis_h:
                visible.add((x, y, h))
                vis_h = h

    # t to b
    for x in range(max_x):
        vis_h = -1
        for y in range(max_y):
            h = grid.get((x, y))
            if h > vis_h:
                visible.add((x, y, h))
                vis_h = h

    # b to t
    for x in range(max_x):
        vis_h = -1
        for y in reversed(range(max_y)):
            h = grid.get((x, y))
            if h > vis_h:
                visible.add((x, y, h))
                vis_h = h

    return len(visible)


def test_day8a():
    assert day8a(example) == 21


def main():
    with open("day08.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 8a", day8a(data))


if __name__ == "__main__":
    main()
