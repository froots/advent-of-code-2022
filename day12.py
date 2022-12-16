example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

import string
from collections import deque

asc = string.ascii_lowercase


def get_h(h):
    if h == "S":
        return 0
    if h == "E":
        return len(asc) - 1
    return h


def get_neighbours(hm, x, y):
    return [
        (x + nx, y + ny)
        for (nx, ny) in ((1, 0), (0, 1), (-1, 0), (0, -1))
        if (x + nx, y + ny) in hm
        and get_h(hm[(x + nx, y + ny)]) <= get_h(hm[(x, y)]) + 1
    ]


def bfs(hm, start, end_test):
    sx, sy = start

    queue = deque([(0, sx, sy)])
    shortest_seen = {start: 0}

    while queue:
        steps, next_x, next_y = queue.popleft()
        next_steps = steps + 1

        if end_test(next_x, next_y):
            break

        for neighbour in get_neighbours(hm, next_x, next_y):
            nx, ny = neighbour
            if neighbour not in shortest_seen or shortest_seen[neighbour] > next_steps:
                shortest_seen[neighbour] = next_steps
                queue.append((next_steps, nx, ny))

    return shortest_seen


def day12a(data):
    rows = data.strip().splitlines()

    hm = {
        (x, y): asc.index(h) if h in asc else h
        for y, row in enumerate(rows)
        for x, h in enumerate(row)
    }

    start = [coords for coords, h in hm.items() if h == "S"][0]
    end = [coords for coords, h in hm.items() if h == "E"][0]

    end_test = lambda x, y: (x, y) == end

    return bfs(hm, start, end_test)[end]


def test_day12a():
    assert day12a(example) == 31


def main():
    with open("day12.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 12a", day12a(data))


if __name__ == "__main__":
    main()
