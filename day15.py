import re

example = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

line_match = re.compile(
    r"Sensor at x=(\-?\d+), y=(\-?\d+)\: closest beacon is at x=(\-?\d+), y=(\-?\d+)"
)


def parse(data):
    pairs = []
    for line in data.strip().splitlines():
        sx, sy, bx, by = (int(n) for n in line_match.match(line).groups())
        pairs.append(((sx, sy), (bx, by), manhattan_distance((sx, sy), (bx, by))))
    return pairs


def manhattan_distance(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)


def row_range(sensor, y):
    (sx, sy), _, mhd = sensor
    inset = mhd - abs(sy - y)
    if inset < 0:
        return None
    return (sx - inset, sx + inset)


def reduce_ranges(ranges):
    if len(ranges) < 2:
        return ranges

    ranges.sort(key=lambda range: range[0])
    final = []

    while True:
        if len(ranges) < 2:
            final += ranges
            break

        (s1, e1), (s2, e2), *rest = ranges

        # Non-contiguous
        if s2 - e1 > 1:
            final.append((s1, e1))
            ranges = [(s2, e2)] + rest
            continue

        # contiguous
        ranges = [(min(s1, s2), max(e1, e2))] + rest

    return final


def day15a(data, y):
    sensors = parse(data)
    ranges = [row_range(sensor, y) for sensor in sensors]
    ranges = reduce_ranges([range for range in ranges if range is not None])

    range_total = sum(end - start + 1 for start, end in ranges)
    beacons_in_row = sum(by == y for _, by in set(beacon for _, beacon, _ in sensors))

    return range_total - beacons_in_row


def test_day15a():
    assert day15a(example, 10) == 26


def test_parse_data():
    data = parse(example)
    assert len(data) == 14
    assert data[0] == ((2, 18), (-2, 15), 7)
    assert data[13] == ((20, 1), (15, 3), 7)


def test_row_range():
    assert row_range(((0, 0), (2, 3), 5), 3) == (-2, 2)
    assert row_range(((-5, 4), (-4, 3), 2), 3) == (-6, -4)


def test_reduce_ranges():
    assert reduce_ranges([(2, 9)]) == [(2, 9)]
    assert reduce_ranges([(2, 5), (7, 9)]) == [(2, 5), (7, 9)]
    assert reduce_ranges([(2, 9), (3, 5)]) == [(2, 9)]
    assert reduce_ranges([(6, 9), (2, 5)]) == [(2, 9)]
    assert reduce_ranges([(2, 5), (3, 9)]) == [(2, 9)]
    assert reduce_ranges([(2, 4), (6, 9), (3, 8)]) == [(2, 9)]
    assert reduce_ranges([(2, 3), (5, 6), (8, 9)]) == [(2, 3), (5, 6), (8, 9)]


def visualise(data):
    sensor_data = parse(data)
    sensors = set((x, y) for (x, y), _, _ in sensor_data)
    beacons = set((x, y) for _, (x, y), _ in sensor_data)

    for y in range(21):
        ranges = [row_range(sensor, y) for sensor in sensor_data]
        ranges = reduce_ranges([r for r in ranges if r is not None])
        row = ""
        for x in range(21):
            current = ""
            if (x, y) in sensors:
                current = "S"
            elif (x, y) in beacons:
                current = "B"
            else:
                for r in ranges:
                    if x in range(r[0], r[1] + 1):
                        current = "#"
                        break
            if not current:
                current = "."
            row += current
        print(row)


def main():
    with open("day15.txt", "r", encoding="utf8") as file:
        data = file.read()
    # print("Visualise", visualise(example))
    print("Day15a", day15a(data, 2000000))


if __name__ == "__main__":
    main()
