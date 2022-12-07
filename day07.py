example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


class Node:
    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = size
        self.total_size = 0

    def add(self, child):
        self.children.append(child)

    def find_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child
        raise ValueError(f"No child with name '{name}' exists")

    def add_size(self, size):
        self.total_size += size
        if self.parent:
            self.parent.add_size(size)

    def __repr__(self):
        return f"<Node {self.name} {self.size}>"


def process_input(data):
    root = Node("/")
    directories = []
    pointer = root

    for line in data.strip().splitlines():
        if line == "$ ls":
            continue
        if line == "$ cd /":
            pointer = root
            continue
        if line == "$ cd ..":
            pointer = pointer.parent
            continue
        if line.startswith("$ cd "):
            pointer = pointer.find_child_by_name(line[5:])
            continue
        if line.startswith("dir "):
            directory = Node(line[4:], parent=pointer)
            pointer.add(directory)
            directories.append(directory)
            continue

        size, name = line.strip().split(" ")
        pointer.add(Node(name, size=int(size), parent=pointer))
        pointer.add_size(int(size))

    return root, directories


def day7a(data):
    __, directories = process_input(data)

    return sum(
        dir.total_size if dir.total_size <= 100_000 else 0 for dir in directories
    )


def test_day7a():
    assert day7a(example) == 95437


def main():
    with open("day07.txt", "r", encoding="utf8") as file:
        data = file.read()
    print("Day 7a", day7a(data))


if __name__ == "__main__":
    main()
