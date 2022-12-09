example = """30373
25512
65332
33549
35390
"""


def parse(data):
    grid = {}

    lines = data.strip().splitlines()

    for y, trees in enumerate(lines):
        for x, tree in enumerate(trees):
            grid[(x, y)] = int(tree)

    return grid, len(lines[0]), len(lines)


def get_sightlines(x, y, grid, breadth, depth):
    north = [(x, sy, grid[(x, sy)]) for sy in reversed(range(y))]
    east = [(sx, y, grid[(sx, y)]) for sx in range(x + 1, breadth)]
    south = [(x, sy, grid[(x, sy)]) for sy in range(y + 1, depth)]
    west = [(sx, y, grid[(sx, y)]) for sx in reversed(range(x))]

    return north, east, south, west


def is_visible(x, y, grid, breadth, depth):
    on_edge = x == 0 or y == 0 or x == breadth - 1 or y == depth - 1

    if on_edge:
        return True

    sightlines = get_sightlines(x, y, grid, breadth, depth)

    return any(
        max(h for _, _, h in sightline) < grid[(x, y)] for sightline in sightlines
    )


def day8a(data):
    grid, breadth, depth = parse(data)

    visible = {
        (x, y, grid[(x, y)])
        for y in range(depth)
        for x in range(breadth)
        if is_visible(x, y, grid, breadth, depth)
    }

    return len(visible)


def test_day8a():
    assert day8a(example) == 21


def test_is_visible():
    grid, breadth, depth = parse(example)

    assert is_visible(1, 1, grid, breadth, depth) is True
    assert is_visible(3, 1, grid, breadth, depth) is False


def main():
    with open("day08.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 8a", day8a(data))


if __name__ == "__main__":
    main()
