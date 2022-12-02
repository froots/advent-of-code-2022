input = """A Y
B X
C Z
"""

VALUES = {"A": 0, "B": 1, "C": 2}


def score_hand(opponent, me):
    mod_diff = (opponent - me) % 3
    if mod_diff == 0:
        return me + 1 + 3
    if mod_diff == 1:
        return me + 1
    return me + 1 + 6


def day2a(input):
    translation = str.maketrans("XYZ", "ABC")
    strategy = [
        (VALUES[line[0]], VALUES[str.translate(line[2], translation)])
        for line in input.strip().splitlines()
    ]
    return sum(score_hand(opponent, me) for opponent, me in strategy)


def test_day2a():
    assert day2a(input) == 15


def test_score_hand():
    assert score_hand(0, 0) == 4  # 0-0 % 3 == 0
    assert score_hand(1, 1) == 5
    assert score_hand(2, 2) == 6

    assert score_hand(0, 1) == 8  # 0-1 % 3 == 2
    assert score_hand(1, 2) == 9  # 1-2 % 3 == 2
    assert score_hand(2, 0) == 7  # 2-0 % 3 == 2

    assert score_hand(0, 2) == 3  # 0-2 % 3 == 1
    assert score_hand(1, 0) == 1  # 1-0 % 3 == 1
    assert score_hand(2, 1) == 2  # 2-1 % 3 == 1


if __name__ == "__main__":
    with open("./day02.txt", "r") as file:
        data = file.read()
        print("Day 2a", day2a(data))
        file.close()
