from itertools import pairwise


example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def parse_rocks(data):
    rocks = set()
    node_pairs = []
    for path in data.strip().splitlines():
        node_pairs += list(
            pairwise(
                [tuple(int(n) for n in node.split(",")) for node in path.split(" -> ")]
            )
        )

    for (node1, node2) in node_pairs:
        x1, y1 = node1
        x2, y2 = node2

        if x1 == x2:
            nodes = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
        if y1 == y2:
            nodes = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
        rocks.update(nodes)

    return rocks


def day14a(data):
    rocks = parse_rocks(data)
    max_y = max(y for x, y in rocks)
    rested = 0
    x, y = (500, 0)

    while True:
        if y > max_y:
            break

        if (x, y + 1) not in rocks:
            y += 1
            continue

        if (x - 1, y + 1) not in rocks:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in rocks:
            x += 1
            y += 1
            continue

        rested += 1
        rocks.add((x, y))
        x, y = (500, 0)

    return rested


def day14b(data):
    rocks = parse_rocks(data)
    max_y = max(y for _, y in rocks)
    floor = max_y + 2
    rested = 0
    x, y = (500, 0)

    while True:
        if (y + 1) == floor:
            rested += 1
            rocks.add((x, y))
            x, y = (500, 0)
            continue

        if (x, y + 1) not in rocks:
            y += 1
            continue

        if (x - 1, y + 1) not in rocks:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in rocks:
            x += 1
            y += 1
            continue

        if (x, y) == (500, 0):
            rested += 1
            break

        rested += 1
        rocks.add((x, y))
        x, y = (500, 0)

    return rested


def test_day14a():
    assert day14a(example) == 24


def test_day14b():
    assert day14b(example) == 93


def test_parse_rocks():
    rocks = parse_rocks(example)
    expected = set(
        [
            (498, 4),
            (498, 5),
            (498, 6),
            (497, 6),
            (496, 6),
            (503, 4),
            (502, 4),
            (502, 5),
            (502, 6),
            (502, 7),
            (502, 8),
            (502, 9),
            (501, 9),
            (500, 9),
            (499, 9),
            (498, 9),
            (497, 9),
            (496, 9),
            (495, 9),
            (494, 9),
        ]
    )
    assert len(rocks) == len(expected)


def main():
    with open("day14.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 14a", day14a(data))
    print("Day 14b", day14b(data))


if __name__ == "__main__":
    main()
