example1 = ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19)
example2 = ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23)
example3 = ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23)
example4 = ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29)
example5 = ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26)


def index_of_unique_chunk(stream, length):
    for end, __ in enumerate(stream.strip()[length - 1 :], length):
        chunk = stream[end - length : end]
        if len(set(chunk)) == length:
            return end
    raise ValueError(f"No unique chunk of length {length} found")


def day6a(stream):
    return index_of_unique_chunk(stream, 4)


def day6b(stream):
    return index_of_unique_chunk(stream, 14)


def test_day6a():
    assert day6a(example1[0]) == example1[1]
    assert day6a(example2[0]) == example2[1]
    assert day6a(example3[0]) == example3[1]
    assert day6a(example4[0]) == example4[1]
    assert day6a(example5[0]) == example5[1]


def test_day6b():
    assert day6b(example2[0]) == example2[2]
    assert day6b(example3[0]) == example3[2]
    assert day6b(example1[0]) == example1[2]
    assert day6b(example4[0]) == example4[2]
    assert day6b(example5[0]) == example5[2]


def main():
    with open("day06.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 6 part 1", day6a(data))
    print("Day 6 part 2", day6b(data))


if __name__ == "__main__":
    main()
