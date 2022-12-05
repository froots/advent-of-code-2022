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


def shared_item(collection=[]):
    shared = set(string.ascii_letters)
    for items in collection:
        shared &= set(items)
    try:
        return shared.pop()
    except:
        raise ValueError("No shared item")


def priority(item):
    return string.ascii_letters.index(item) + 1


def day3a(rucksacks):
    return sum(
        priority(shared_item(split_contents(line)))
        for line in rucksacks.strip().splitlines()
    )


def day3b(rucksacks):
    rucksacks = rucksacks.strip().splitlines()
    return sum(
        priority(shared_item(group))
        for group in [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]
    )


def test_day3a():
    assert day3a(example) == 157


def test_day3b():
    assert day3b(example) == 70


def test_split_contents():
    assert split_contents("vJrwpWtwJgWrhcsFMMfFFhFp") == (
        "vJrwpWtwJgWr",
        "hcsFMMfFFhFp",
    )


def test_shared_item():
    assert shared_item(["vJrwpWtwJgWr", "hcsFMMfFFhFp"]) == "p"
    assert (
        shared_item(
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ]
        )
        == "r"
    )


def test_priority():
    assert priority("p") == 16
    assert priority("L") == 38


def run():
    with open("day03.txt", "r", encoding="utf8") as file:
        data = file.read()
        print("Day 3a", day3a(data))
        print("Day 3b", day3b(data))
        file.close()


if __name__ == "__main__":
    run()
