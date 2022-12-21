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
    return ranges


def day15a(data, y):
    sensors = parse(data)

    ranges = [row_range(sensor, y) for sensor in sensors]
    ranges = [range for range in ranges if range is not None]

    print(ranges)

    # Merge ranges
    # Calculate total length of all ranges
    # Remove any beacons in the selected row from the count


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
    assert reduce_ranges([(2, 15)]) == [(2, 15)]
