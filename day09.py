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


def move_head(current, direction, distance):
    x, y = current
    dx, dy = DIRECTIONS[direction]
    return (x + dx * distance, y + dy * distance)


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


def day9a(data):
    head = (0, 0)
    tail = (0, 0)
    tail_locations = set([tail])

    # for each command
    for line in data.strip().splitlines():
        direction = line[0]
        distance = int(line[2:])

        head = move_head(head, direction, distance)
        tail, locations = move_tail(tail, head)
        tail_locations |= locations

    # return the number of locations
    return len(tail_locations)


def test_day9a():
    assert day9a(example) == 13


def test_move_tail():
    assert move_tail((1, 1), (1, 1))[0] == (1, 1)  # Stays when in same location
    assert move_tail((1, 1), (2, 1))[0] == (1, 1)  # Stays when 1 away
    assert move_tail((1, 1), (1, 2))[0] == (1, 1)  # Stays when 1 away
    assert move_tail((1, 1), (2, 2))[0] == (1, 1)  # Stays when 1 away diagonally

    assert move_tail((1, 1), (3, 1))[0] == (2, 1)  # Moves to be one away
    assert move_tail((1, 1), (4, 1))[0] == (3, 1)  # Moves to be one away
    assert move_tail((5, 5), (5, 2))[0] == (5, 3)  # Moves to be one away

    # Moves diagonally first, then within one
    assert move_tail((3, 3), (6, 4))[0] == (5, 4)


def main():
    with open("day09.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 9a", day9a(data))


if __name__ == "__main__":
    main()
