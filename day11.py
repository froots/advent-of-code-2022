example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


class Monkey:
    @staticmethod
    def parse_many(data):
        return {
            m_id: Monkey.parse(monkey_data)
            for m_id, monkey_data in enumerate(data.strip().split("\n\n"))
        }

    @staticmethod
    def parse(data):
        lines = data.strip().splitlines()

        monkey_id = int(lines[0].removeprefix("Monkey ").removesuffix(":"))

        items = [
            int(item)
            for item in lines[1].removeprefix("  Starting items: ").split(", ")
        ]

        operation_text = lines[2].removeprefix("  Operation: new = old ")
        operation = operation_text[0]
        operand = operation_text[2:]

        divisibility_test = int(lines[3].removeprefix("  Test: divisible by "))

        true_monkey = int(lines[4].removeprefix("    If true: throw to monkey "))
        false_monkey = int(lines[5].removeprefix("    If false: throw to monkey "))

        return Monkey(
            monkey_id,
            items=items,
            operation=operation,
            operand=operand,
            divisibility_test=divisibility_test,
            true_monkey=true_monkey,
            false_monkey=false_monkey,
        )

    def __init__(
        self,
        monkey_id,
        items=None,
        operation="+",
        operand=1,
        divisibility_test=1,
        true_monkey=None,
        false_monkey=None,
    ):
        if items is None:
            items = []
        self.id = monkey_id
        self.items = items
        self.operation = operation
        self.divisibility_test = divisibility_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_count = 0

        if operand == "old":
            self.operand = "old"
        else:
            self.operand = int(operand)

    def operate(self, worry):
        operand = worry if self.operand == "old" else self.operand
        return worry * operand if self.operation == "*" else worry + operand

    def choose_monkey(self, worry):
        return (
            self.true_monkey
            if worry % self.divisibility_test == 0
            else self.false_monkey
        )

    def turn(self, worry_management_factor=3):
        items_thrown = []
        for item in self.items:
            worry = self.operate(item) // worry_management_factor
            target_monkey = self.choose_monkey(worry)
            items_thrown.append((target_monkey, worry))
        self.inspect_count += len(self.items)
        self.items = []
        return items_thrown

    def add_item(self, worry):
        self.items.append(worry)


def pass_items(thrown_items, monkeys):
    for monkey_id, worry in thrown_items:
        monkeys.get(monkey_id).add_item(worry)


def run_rounds(monkeys, rounds, worry_management_factor=3):
    for _ in range(rounds):
        for monkey in monkeys.values():
            pass_items(monkey.turn(worry_management_factor), monkeys)

    return monkeys


def day11a(data):
    monkeys = Monkey.parse_many(data)
    monkeys = run_rounds(monkeys, 20)

    most_active = sorted(monkey.inspect_count for monkey in monkeys.values())

    return most_active[-1] * most_active[-2]


def test_day11a():
    assert day11a(example) == 10605


def test_parse_monkey():
    monkey = Monkey.parse(example.split("\n\n")[0])
    assert monkey.items == [79, 98]
    assert monkey.id == 0
    assert monkey.operation == "*"
    assert monkey.operand == 19
    assert monkey.divisibility_test == 23
    assert monkey.true_monkey == 2
    assert monkey.false_monkey == 3


def test_parse_monkey_with_old_operand():
    monkey = Monkey.parse(example.split("\n\n")[2])
    assert monkey.items == [79, 60, 97]
    assert monkey.id == 2
    assert monkey.operation == "*"
    assert monkey.operand == "old"
    assert monkey.divisibility_test == 13
    assert monkey.true_monkey == 1
    assert monkey.false_monkey == 3


def test_monkey_turn():
    monkey = Monkey.parse(example.split("\n\n")[0])
    items_thrown = monkey.turn()
    assert items_thrown == [(3, 500), (3, 620)]

    monkey2 = Monkey.parse(example.split("\n\n")[2])
    items_thrown = monkey2.turn()
    assert items_thrown == [(1, 2080), (3, 1200), (3, 3136)]


def test_monkey_rounds_1():
    monkeys = Monkey.parse_many(example)

    monkeys = run_rounds(monkeys, 1)

    assert monkeys.get(0).items == [20, 23, 27, 26]
    assert monkeys.get(1).items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys.get(2).items == []
    assert monkeys.get(3).items == []


def test_monkey_rounds_2():
    monkeys = Monkey.parse_many(example)

    monkeys = run_rounds(monkeys, 2)

    assert monkeys.get(0).items == [695, 10, 71, 135, 350]
    assert monkeys.get(1).items == [43, 49, 58, 55, 362]
    assert monkeys.get(2).items == []
    assert monkeys.get(3).items == []


def test_monkey_rounds_3():
    monkeys = Monkey.parse_many(example)

    monkeys = run_rounds(monkeys, 3)

    assert monkeys.get(0).items == [16, 18, 21, 20, 122]
    assert monkeys.get(1).items == [1468, 22, 150, 286, 739]
    assert monkeys.get(2).items == []
    assert monkeys.get(3).items == []


def test_monkey_rounds_20():
    monkeys = Monkey.parse_many(example)

    monkeys = run_rounds(monkeys, 20)

    assert monkeys.get(0).items == [10, 12, 14, 26, 34]
    assert monkeys.get(1).items == [245, 93, 53, 199, 115]
    assert monkeys.get(2).items == []
    assert monkeys.get(3).items == []


def main():
    with open("day11.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 11a", day11a(data))


if __name__ == "__main__":
    main()
