example1 = ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7)
example2 = ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5)
example3 = ("nppdvjthqldpwncqszvftbrmjlhg", 6)
example4 = ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10)
example5 = ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)


def day6a(stream):
    for end, __ in enumerate(stream.strip()[3:], 4):
        chunk = stream[end - 4 : end]
        if len(set(chunk)) == 4:
            return end
    raise ValueError("No start of packet marker present")


def test_day6a():
    assert day6a(example1[0]) == example1[1]
    assert day6a(example2[0]) == example2[1]
    assert day6a(example3[0]) == example3[1]
    assert day6a(example4[0]) == example4[1]
    assert day6a(example5[0]) == example5[1]


def main():
    with open("day06.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 6 part 1", day6a(data))


if __name__ == "__main__":
    main()
