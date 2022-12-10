example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

DIRECTIONS = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}


def move_tail(tail, head):
    tx, ty = tail
    hx, hy = head

    locations = set()

    while max(abs(hx - tx), abs(hy - ty)) > 1:
        dx = hx - tx
        dy = hy - ty

        if dx != 0:
            tx += dx // abs(dx)

        if dy != 0:
            ty += dy // abs(dy)

        locations.add((tx, ty))

    return (tx, ty), locations


def move_command(direction, distance, head, tails):
    locations = set()
    dx, dy = DIRECTIONS[direction]
    hx, hy = head
    # For range of head moves
    for d in range(distance):
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


def day9a(data):
    head = (0, 0)
    tails = [(0, 0)]

    last_tail_locations = set(tails[-1])

    for line in data.strip().splitlines():
        head, tails, locations = move_command(line[0], int(line[2:]), head, tails)

        last_tail_locations |= locations

    return len(last_tail_locations)


def test_day9a():
    assert day9a(example) == 13


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


if __name__ == "__main__":
    main()
