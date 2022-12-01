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


def day1a(input):
    totals = []
    total = 0
    for line in input.splitlines():
        if line:
            total += int(line)
        else:
            totals.append(total)
            total = 0
    totals.append(total)
    return max(totals)


def test_day1a():
    assert day1a(input) == 24_000


if __name__ == "__main__":
    with open("./day1.txt", "r") as file:
        data = file.read()
        print("Day 1a", day1a(data))
        file.close()
