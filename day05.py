import re

example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

move_matcher = re.compile(r"move (\d+) from (\d+) to (\d+)")


def parse_stacks(data):
    stacks = [
        [line[i + 1 : i + 2] for i in range(0, len(line), 4)]
        for line in data.split("\n")
    ][0:-1]

    return ["".join(stack[::-1]).rstrip() for stack in zip(*stacks)]


def parse_moves(data):
    return [
        tuple(int(n) for n in move_matcher.match(move).groups())
        for move in data.splitlines()
    ]


def parse(data):
    stacks, moves = data.rstrip().split("\n\n")
    return parse_stacks(stacks), parse_moves(moves)


def test_parse():
    stacks, moves = parse(example)
    assert stacks == ["ZN", "MCD", "P"]

    assert moves[0] == (1, 2, 1)
    assert moves[1] == (3, 1, 3)
    assert moves[2] == (2, 2, 1)
    assert moves[3] == (1, 1, 2)
