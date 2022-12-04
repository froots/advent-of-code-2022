example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def ranges(pair):
    return tuple(tuple(int(n) for n in range.split("-")) for range in pair.split(","))


def range_set(r):
    start, end = r
    return set(range(start, end + 1))


def is_contained(a, b):
    a_set = range_set(a)
    b_set = range_set(b)
    return len(a_set & b_set) == min(len(a_set), len(b_set))


def is_overlapping(a, b):
    a_set = range_set(a)
    b_set = range_set(b)
    return len(a_set | b_set) < len(a_set) + len(b_set)


def day4a(data):
    return sum(is_contained(*ranges(line)) for line in data.strip().splitlines())


def day4b(data):
    return sum(is_overlapping(*ranges(line)) for line in data.strip().splitlines())


def test_day4a():
    assert day4a(example) == 2


def test_day4b():
    assert day4b(example) == 4


def test_ranges():
    assert ranges("2-4,6-8") == ((2, 4), (6, 8))
    assert ranges("30-34,42-56") == ((30, 34), (42, 56))


def test_is_contained():
    assert is_contained((2, 3), (4, 5)) is False
    assert is_contained((2, 4), (4, 5)) is False
    assert is_contained((5, 7), (6, 7)) is True
    assert is_contained((5, 5), (3, 5)) is True
    assert is_contained((2, 4), (2, 4)) is True


def test_is_overlapping():
    assert is_overlapping((2, 4), (6, 8)) is False
    assert is_overlapping((2, 3), (4, 5)) is False
    assert is_overlapping((5, 7), (7, 9)) is True
    assert is_overlapping((2, 8), (3, 7)) is True
    assert is_overlapping((6, 6), (4, 6)) is True
    assert is_overlapping((2, 6), (4, 8)) is True


if __name__ == "__main__":
    with open("day04.txt", "r", encoding="utf8") as file:
        data = file.read()
        print("Day 4a", day4a(data))
        print("Day 4b", day4b(data))
        file.close()
