import functools

example = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


def compare(a, b):

    if isinstance(a, int) and isinstance(b, int):
        return b - a

    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])

    if len(a) and len(b):
        next_a, a = a[0], a[1:]
        next_b, b = b[0], b[1:]
        c = compare(next_a, next_b)
        return compare(a, b) if c == 0 else c

    return len(b) - len(a)


def day13a(data):
    packets = [
        tuple(eval(packet) for packet in pair.split("\n"))
        for pair in data.strip().split("\n\n")
    ]

    orders = {i + 1: compare(*pair) for i, pair in enumerate(packets)}

    return sum(i for i, order in orders.items() if order >= 1)


def day13b(data):
    packets = [eval(packet) for packet in data.strip().split("\n") if packet]
    dividers = [[[2]], [[6]]]
    packets.extend(dividers)
    packets.sort(key=functools.cmp_to_key(compare), reverse=True)

    i1, i2 = (i + 1 for i, packet in enumerate(packets) if packet in dividers)

    return i1 * i2


def test_day13a():
    assert day13a(example) == 13


def test_day13b():
    assert day13b(example) == 140


def test_compare_bare_integers():
    assert compare(1, 3) >= 1
    assert compare(3, 1) <= -1
    assert compare(1, 1) == 0


def test_compare_integer_lists_with_one_item():
    assert compare([1], [3]) >= 1
    assert compare([3], [1]) <= -1
    assert compare([1], [1]) == 0


def test_compare_integer_lists_with_equal_length():
    assert compare([1, 2], [1, 3]) >= 1
    assert compare([3, 2, 1], [3, 1, 3]) <= -1
    assert compare([1, 2, 3], [1, 2, 3]) == 0


def test_compare_integer_with_list():
    assert compare([3], 3) == 0
    assert compare(3, [3]) == 0
    assert compare(3, [4]) >= 1
    assert compare([3], 4) >= 1
    assert compare(4, [3]) <= -1
    assert compare([4], 3) <= -1


def test_compare_lists_with_unequal_length():
    assert compare([1, 2, 3], [1, 2]) <= -1
    assert compare([1, 2], [1, 2, 3]) >= 1


def test_compare_examples():
    assert compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) >= 1
    assert compare([[1], [2, 3, 4]], [[1], 4]) >= 1
    assert compare([9], [[8, 7, 6]]) <= -1
    assert compare([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) >= 1
    assert compare([7, 7, 7, 7], [7, 7, 7]) <= -1
    assert compare([], [3]) >= 1
    assert compare([[[]]], [[]]) <= -1

    left = [1, [2, [3, [4, [5, 6, 7]]]], 8, 9]
    right = [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]

    assert compare(left, right) <= -1


def main():
    with open("day13.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 13a", day13a(data))
    print("Day 13b", day13b(data))


if __name__ == "__main__":
    main()
