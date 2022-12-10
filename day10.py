# Cycles of a clock circuit
# Single register X with starting value 1
# Two instructions:
#   'addx V' - 2 cycles - after 2 cycles, X increased by value V
#   'noop' - 1 cycle

example1 = """noop
addx 3
addx -5
"""

example2 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""


def pos_after_cycle(cycle, log):
    return [value for c, value in log if c <= cycle][-1]


def create_register_log(data):
    completed_cycles = 0
    register_x = 1
    log = [(0, 1)]

    for cmd in data.strip().splitlines():
        if cmd == "noop":
            completed_cycles += 1
            continue
        register_x += int(cmd[5:])
        completed_cycles += 2
        log.append((completed_cycles, register_x))

    return log


def day10a(data):
    reg_x_log = create_register_log(data)

    return sum(
        (cycle + 1) * pos_after_cycle(cycle, reg_x_log)
        for cycle in range(19, max(c for c, _ in reg_x_log), 40)
    )


def test_day10a():
    assert day10a(example2) == 13140


def main():
    with open("day10.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 10a", day10a(data))


if __name__ == "__main__":
    main()
