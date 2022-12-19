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

    print(node_pairs)

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
    # parse rock structure
    # while abyss not been hit
    # drop sand item until it comes to rest according to rules
    # return number of rested sand items
    pass


# def test_day14a():
#     assert day14a(example) == 24


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
