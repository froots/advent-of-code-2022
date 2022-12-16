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
    if x == 0 or y == 0 or x == breadth - 1 or y == depth - 1:
        return True

    sightlines = get_sightlines(x, y, grid, breadth, depth)

    return any(
        max(h for _, _, h in sightline) < grid[(x, y)] for sightline in sightlines
    )


def scenic_score(x, y, grid, breadth, depth):
    sightlines = get_sightlines(x, y, grid, breadth, depth)
    height = grid[(x, y)]
    score = 1

    for sightline in sightlines:
        if len(sightline) == 0:
            return 0
        for no_trees, (sx, sy, h) in enumerate(sightline, 1):
            if h >= height or no_trees == len(sightline):
                score *= no_trees
                break

    return score


def day8a(data):
    grid, breadth, depth = parse(data)

    visible = {
        (x, y, grid[(x, y)])
        for y in range(depth)
        for x in range(breadth)
        if is_visible(x, y, grid, breadth, depth)
    }

    return len(visible)


def day8b(data):
    grid, breadth, depth = parse(data)

    return max(scenic_score(x, y, grid, breadth, depth) for (x, y), _ in grid.items())


def test_day8a():
    assert day8a(example) == 21


def test_day8b():
    assert day8b(example) == 8


def test_is_visible():
    grid, breadth, depth = parse(example)

    assert is_visible(1, 1, grid, breadth, depth) is True
    assert is_visible(3, 1, grid, breadth, depth) is False


def test_scenic_score():
    grid, breadth, depth = parse(example)

    assert scenic_score(0, 0, grid, breadth, depth) == 0
    assert scenic_score(2, 1, grid, breadth, depth) == 4
    assert scenic_score(2, 3, grid, breadth, depth) == 8


def main():
    with open("day08.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 8a", day8a(data))
    print("Day 8b", day8b(data))


if __name__ == "__main__":
    main()
