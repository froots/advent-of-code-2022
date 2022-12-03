input = """A Y
B X
C Z
"""

VALUES = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
WIN = 6
DRAW = 3
LOSE = 0


def score_hand(opponent, me):
    opponent = VALUES[opponent]
    me = VALUES[me]
    mod_diff = (opponent - me) % 3
    if mod_diff == 0:
        return me + 1 + DRAW
    if mod_diff == 1:
        return me + 1 + LOSE
    return me + 1 + WIN


def day2a(input):
    return sum(score_hand(line[0], line[2]) for line in input.strip().splitlines())


# def day2b(input):
#     strategy = [
#         (VALUES[line[0]], adjust(line[2], line[0])])
#     ]


def test_day2a():
    assert day2a(input) == 15


# def test_day2b():
#     assert day2b(input) == 12


def test_score_hand():
    assert score_hand("A", "X") == 4  # 0-0 % 3 == 0
    assert score_hand("B", "Y") == 5
    assert score_hand("C", "Z") == 6

    assert score_hand("A", "Y") == 8  # 0-1 % 3 == 2
    assert score_hand("B", "Z") == 9  # 1-2 % 3 == 2
    assert score_hand("C", "X") == 7  # 2-0 % 3 == 2

    assert score_hand("A", "Z") == 3  # 0-2 % 3 == 1
    assert score_hand("B", "X") == 1  # 1-0 % 3 == 1
    assert score_hand("C", "Y") == 2  # 2-1 % 3 == 1


if __name__ == "__main__":
    with open("./day02.txt", "r") as file:
        data = file.read()
        print("Day 2a", day2a(data))
        file.close()
