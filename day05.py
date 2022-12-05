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


def arrange(stacks, move, multi=False):
    count, origin, destination = move
    if multi:
        to_move = stacks[origin - 1][-count:]
    else:
        to_move = stacks[origin - 1][-1 : -1 - count : -1]
    to_remain = stacks[origin - 1][0:-count]
    stacks[destination - 1] += to_move
    stacks[origin - 1] = to_remain
    return stacks


def day5a(data):
    stacks, moves = parse(data)

    for move in moves:
        stacks = arrange(stacks, move)

    return "".join(stack[-1] for stack in stacks)


def day5b(data):
    stacks, moves = parse(data)

    for move in moves:
        stacks = arrange(stacks, move, multi=True)

    return "".join(stack[-1] for stack in stacks)


def test_parse():
    stacks, moves = parse(example)
    assert stacks == ["ZN", "MCD", "P"]

    assert moves[0] == (1, 2, 1)
    assert moves[1] == (3, 1, 3)
    assert moves[2] == (2, 2, 1)
    assert moves[3] == (1, 1, 2)


def test_day5a():
    assert day5a(example) == "CMZ"


def test_day5b():
    assert day5b(example) == "MCD"


def run():
    with open("day05.txt", "r", encoding="utf8") as file:
        data = file.read()
        print("Day 5a", day5a(data))
        print("Day 5b", day5b(data))
        file.close()


if __name__ == "__main__":
    run()
