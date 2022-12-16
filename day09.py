example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

DIRECTIONS = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}


def move_command(direction, distance, head, tails):
    locations = set()
    dx, dy = DIRECTIONS[direction]
    hx, hy = head
    # For range of head moves
    for _ in range(distance):
        # move head one
        hx += dx
        hy += dy
        head = (hx, hy)

        # move each tail according to the head / tail in front
        for t, (tx, ty) in enumerate(tails):
            leader = head if t == 0 else tails[t - 1]
            lx, ly = leader

            # Only move if planck distance to leader > 1
            if max(abs(lx - tx), abs(ly - ty)) > 1:
                tx += (lx - tx) // (abs(lx - tx) or 1)
                ty += (ly - ty) // (abs(ly - ty) or 1)
                tails[t] = (tx, ty)
                if t == len(tails) - 1:
                    locations.add((tx, ty))

    return (hx, hy), tails, locations


def calculate_no_of_last_tail_locations(data, tail_count=1):
    head = (0, 0)
    tails = [(0, 0)] * tail_count

    last_tail_locations = set(tails[-1])

    for line in data.strip().splitlines():
        head, tails, locations = move_command(line[0], int(line[2:]), head, tails)

        last_tail_locations |= locations

    return len(last_tail_locations)


def day9a(data):
    return calculate_no_of_last_tail_locations(data)


def day9b(data):
    return calculate_no_of_last_tail_locations(data, 9)


def test_day9a():
    assert day9a(example) == 13


def test_day9b():
    assert day9b(example) == 1
    assert day9b(example2) == 36


def test_move_command_with_one_tail():
    head = (0, 0)
    tails = [(0, 0)]

    head, tails, locations = move_command("U", 3, head, tails)
    assert head == (0, 3)
    assert tails[0] == (0, 2)
    assert len(locations) == 2
    assert (0, 1) in locations
    assert (0, 2) in locations


def main():
    with open("day09.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 9a", day9a(data))
    print("Day 9b", day9b(data))


if __name__ == "__main__":
    main()
