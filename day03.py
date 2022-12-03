import string

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def split_contents(sack):
    n = len(sack) // 2
    return (sack[:n], sack[n:])


def shared_item(a, b):
    shared = set(a) & set(b)
    try:
        return shared.pop()
    except:
        raise ValueError("No shared item")


def priority(item):
    return string.ascii_letters.index(item) + 1


def day3a(rucksacks):
    return sum(
        priority(shared_item(*split_contents(line)))
        for line in rucksacks.strip().splitlines()
    )


def test_day3a():
    assert day3a(example) == 157


def test_split_contents():
    assert split_contents("vJrwpWtwJgWrhcsFMMfFFhFp") == (
        "vJrwpWtwJgWr",
        "hcsFMMfFFhFp",
    )


def test_shared_item():
    assert shared_item("vJrwpWtwJgWr", "hcsFMMfFFhFp") == "p"


def test_priority():
    assert priority("p") == 16
    assert priority("L") == 38


if __name__ == "__main__":
    with open("day03.txt", "r", encoding="utf8") as file:
        data = file.read()
        print("Day 3a", day3a(data))
        file.close()
