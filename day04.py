example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def ranges(pair):
    return tuple(tuple(int(n) for n in range.split("-")) for range in pair.split(","))


def is_contained(a, b):
    a_start, a_end = a
    b_start, b_end = b
    a_set = set(range(a_start, a_end + 1))
    b_set = set(range(b_start, b_end + 1))
    return len(a_set & b_set) == min(len(a_set), len(b_set))


def day4a(data):
    return sum(is_contained(*ranges(line)) for line in data.strip().splitlines())


def test_day4a():
    assert day4a(example) == 2


def test_ranges():
    assert ranges("2-4,6-8") == ((2, 4), (6, 8))
    assert ranges("30-34,42-56") == ((30, 34), (42, 56))


def test_is_contained():
    assert is_contained((2, 3), (4, 5)) == False
    assert is_contained((2, 4), (4, 5)) == False
    assert is_contained((5, 7), (6, 7)) == True
    assert is_contained((5, 5), (3, 5)) == True
    assert is_contained((2, 4), (2, 4)) == True


if __name__ == "__main__":
    with open("day04.txt", "r", encoding="utf8") as file:
        data = file.read()
        print("Day 4a", day4a(data))
        file.close()
