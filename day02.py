example = """A Y
B X
C Z
"""

VALUES = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
WIN = 6
DRAW = 3
LOSE = 0
RESULT_ADJUST = [2, 0, 1]


def score(opponent, me):
    mod_diff = (opponent - me) % 3
    if mod_diff == 0:
        return me + 1 + DRAW
    if mod_diff == 1:
        return me + 1 + LOSE
    return me + 1 + WIN


def score_hand_a(opponent, me):
    return score(VALUES[opponent], VALUES[me])


def score_hand_b(opponent, result):
    opponent = VALUES[opponent]
    me = (opponent + RESULT_ADJUST[VALUES[result]]) % 3
    return score(opponent, me)


def day2a(strategy):
    return sum(score_hand_a(line[0], line[2]) for line in strategy.strip().splitlines())


def day2b(strategy):
    return sum(score_hand_b(line[0], line[2]) for line in strategy.strip().splitlines())


def test_day2a():
    assert day2a(example) == 15


def test_day2b():
    assert day2b(example) == 12


def test_score_hand_a():
    assert score_hand_a("A", "X") == 4
    assert score_hand_a("B", "Y") == 5
    assert score_hand_a("C", "Z") == 6

    assert score_hand_a("A", "Y") == 8
    assert score_hand_a("B", "Z") == 9
    assert score_hand_a("C", "X") == 7

    assert score_hand_a("A", "Z") == 3
    assert score_hand_a("B", "X") == 1
    assert score_hand_a("C", "Y") == 2


def test_score_hand_b():
    assert score_hand_b("A", "Y") == 4
    assert score_hand_b("B", "X") == 1
    assert score_hand_b("C", "Z") == 7


def main():
    with open("./day02.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 2a", day2a(data))
    print("Day 2b", day2b(data))


if __name__ == "__main__":
    main()
