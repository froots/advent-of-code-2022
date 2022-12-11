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

        if operand == "old":
            self.operand = "old"
        else:
            self.operand = int(operand)


def day11a(data):
    # parse monkey details into class instances

    # for 20 rounds
    #   process each monkey
    pass


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
