FILENAME = "demo.txt"  # expected 2713310158
FILENAME = "input.txt"

ROUND_COUNT = 10000


def main() -> None:
    monkeys: list[tuple[list[int], tuple[int, int, int], int, tuple[int, int]]] = []
    flush_number = 1
    monkey_count = []
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                continue
            if line.startswith("Monkey"):
                if len(monkeys) != int(line.split(" ")[1][:-1]):
                    raise NotImplementedError
                monkeys.append(([], (0, 0, 0), 0, (0, 0)))
                monkey_count.append(0)
            elif line.startswith("Starting items:"):
                monkeys[-1] = (
                    list(map(int, line.split(": ")[1].split(", "))),
                    monkeys[-1][1],
                    monkeys[-1][2],
                    monkeys[-1][3],
                )
            elif line.startswith("Operation:"):
                ops = line.split(" ")
                if ops[4] == "+":
                    if ops[3] == "old" and ops[5].isdigit():
                        operation = (0, 1, int(ops[5]))
                    else:
                        raise NotImplementedError
                elif ops[4] == "*":
                    if ops[3] == "old" and ops[5] == "old":
                        operation = (1, 0, 0)
                    elif ops[3] == "old" and ops[5].isdigit():
                        operation = (0, int(ops[5]), 0)
                    else:
                        raise NotImplementedError
                else:
                    raise NotImplementedError
                monkeys[-1] = (
                    monkeys[-1][0],
                    operation,
                    monkeys[-1][2],
                    monkeys[-1][3],
                )
            elif line.startswith("Test:"):
                monkeys[-1] = (
                    monkeys[-1][0],
                    monkeys[-1][1],
                    int(line.split(" ")[3]),
                    monkeys[-1][3],
                )
                flush_number *= int(line.split(" ")[3])
            elif line.startswith("If true:"):
                monkeys[-1] = (
                    monkeys[-1][0],
                    monkeys[-1][1],
                    monkeys[-1][2],
                    (int(line.split(" ")[5]), monkeys[-1][3][1]),
                )
            elif line.startswith("If false:"):
                monkeys[-1] = (
                    monkeys[-1][0],
                    monkeys[-1][1],
                    monkeys[-1][2],
                    (monkeys[-1][3][0], int(line.split(" ")[5])),
                )
            else:
                print(line)
                raise NotImplementedError
    for _ in range(ROUND_COUNT):
        for index, monkey in enumerate(monkeys):
            while len(monkey[0]) > 0:
                item = monkey[0].pop()
                item = item * item * monkey[1][0] + item * monkey[1][1] + monkey[1][2]
                item = item % flush_number
                if item % monkey[2] == 0:
                    monkeys[monkey[3][0]][0].append(item)
                else:
                    monkeys[monkey[3][1]][0].append(item)
                monkey_count[index] += 1
    monkey_count.sort()
    print(monkey_count[-1] * monkey_count[-2])


if __name__ == "__main__":
    main()
