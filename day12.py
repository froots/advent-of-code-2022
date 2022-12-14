example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

import string
from collections import deque

asc = string.ascii_lowercase


def parse_map(data):
    return {
        (x, y): asc.index(h) if h in asc else h
        for y, row in enumerate(data.strip().splitlines())
        for x, h in enumerate(row)
    }


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


def bfs(hm, start, end):
    sx, sy = start

    queue = deque([(0, sx, sy)])
    shortest_seen = {start: 0}

    while queue:
        steps, next_x, next_y = queue.popleft()
        next_steps = steps + 1

        if (next_x, next_y) == end:
            break

        for neighbour in get_neighbours(hm, next_x, next_y):
            nx, ny = neighbour
            if neighbour not in shortest_seen or shortest_seen[neighbour] > next_steps:
                shortest_seen[neighbour] = next_steps
                queue.append((next_steps, nx, ny))

    return shortest_seen[end] if end in shortest_seen else None


def day12a(data):
    hm = parse_map(data)
    start = [coords for coords, h in hm.items() if h == "S"][0]
    end = [coords for coords, h in hm.items() if h == "E"][0]
    return bfs(hm, start, end)


def day12b(data):
    hm = parse_map(data)
    end = [coords for coords, h in hm.items() if h == "E"][0]
    starts = [coords for coords, h in hm.items() if h == "S" or h == 0]

    results = [bfs(hm, start, end) for start in starts]
    return min(result for result in results if result is not None)


def test_day12a():
    assert day12a(example) == 31


def test_day12b():
    assert day12b(example) == 29


def main():
    with open("day12.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 12a", day12a(data))
    print("Day 12b", day12b(data))


if __name__ == "__main__":
    main()
