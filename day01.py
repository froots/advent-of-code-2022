input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

"""


def totals(input):
    groups = [group.split("\n") for group in input.strip().split("\n\n")]
    return sorted(sum([int(item) for item in group]) for group in groups)[::-1]


def day1a(input):
    return totals(input)[0]


def day1b(input):
    return sum(totals(input)[0:3])


def test_day1a():
    assert day1a(input) == 24_000


def test_day1b():
    assert day1b(input) == 45_000


def run():
    with open("./day01.txt", "r") as file:
        data = file.read()
        print("Day 1a", day1a(data))
        print("Day 1b", day1b(data))
        file.close()


if __name__ == "__main__":
    run()
