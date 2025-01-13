import re

# FILENAME, WIRE = "demo1.txt", "d"  # expected 72
# FILENAME, WIRE = "demo1.txt", "e"  # expected 507
# FILENAME, WIRE = "demo1.txt", "f"  # expected 492
# FILENAME, WIRE = "demo1.txt", "g"  # expected 114
# FILENAME, WIRE = "demo1.txt", "h"  # expected 65412
# FILENAME, WIRE = "demo1.txt", "i"  # expected 65079
# FILENAME, WIRE = "demo1.txt", "x"  # expected 123
# FILENAME, WIRE = "demo1.txt", "y"  # expected 456
FILENAME, WIRE = "input.txt", "a"
MAX = 65535
EQUAL = "EQUAL"
AND = "AND"
OR = "OR"
LSHIFT = "LSHIFT"
RSHIFT = "RSHIFT"
NOT = "NOT"


def f(
    data: tuple[int | str, ...],
    wires: dict[str, int],
    gates_queue: set[tuple[str | int, ...]],
) -> bool:
    if data[0] == EQUAL:
        if isinstance(data[1], int) or data[1].isnumeric():
            a = int(data[1])
        elif data[1] in wires:
            a = wires[data[1]]
        else:
            gates_queue.add(data)
            return False
        if data[2] in wires or isinstance(data[2], int):
            raise NotImplementedError
        wires[data[2]] = a
        return True
    if data[0] == AND:
        if isinstance(data[1], int) or data[1].isnumeric():
            a = int(data[1])
        elif data[1] in wires:
            a = wires[data[1]]
        else:
            gates_queue.add(data)
            return False
        if isinstance(data[2], int) or data[2].isnumeric():
            b = int(data[2])
        elif data[2] in wires:
            b = wires[data[2]]
        else:
            gates_queue.add(data)
            return False
        if data[3] in wires or isinstance(data[3], int):
            raise NotImplementedError
        wires[data[3]] = a & b
        return True
    if data[0] == OR:
        if isinstance(data[1], int) or data[1].isnumeric():
            a = int(data[1])
        elif data[1] in wires:
            a = wires[data[1]]
        else:
            gates_queue.add(data)
            return False
        if isinstance(data[2], int) or data[2].isnumeric():
            b = int(data[2])
        elif data[2] in wires:
            b = wires[data[2]]
        else:
            gates_queue.add(data)
            return False
        if data[3] in wires or isinstance(data[3], int):
            raise NotImplementedError
        wires[data[3]] = a | b
        return True
    if data[0] == LSHIFT:
        if isinstance(data[1], int) or data[1].isnumeric():
            a = int(data[1])
        elif data[1] in wires:
            a = wires[data[1]]
        else:
            gates_queue.add(data)
            return False
        if isinstance(data[2], int) or data[2].isnumeric():
            b = int(data[2])
        else:
            raise NotImplementedError
        if data[3] in wires or isinstance(data[3], int):
            raise NotImplementedError
        wires[data[3]] = a << int(b)
        return True
    if data[0] == RSHIFT:
        if isinstance(data[1], int) or data[1].isnumeric():
            a = int(data[1])
        elif data[1] in wires:
            a = wires[data[1]]
        else:
            gates_queue.add(data)
            return False
        if isinstance(data[2], int) or data[2].isnumeric():
            b = int(data[2])
        else:
            raise NotImplementedError
        if data[3] in wires or isinstance(data[3], int):
            raise NotImplementedError
        wires[data[3]] = a >> int(b)
        return True
    if data[0] == NOT:
        if isinstance(data[1], int) or data[1].isnumeric():
            a = int(data[1])
        elif data[1] in wires:
            a = wires[data[1]]
        else:
            gates_queue.add(data)
            return False
        if data[2] in wires or isinstance(data[2], int):
            raise NotImplementedError
        wires[data[2]] = MAX - a
        return True
    print(f"data = {data}")
    raise NotImplementedError


def main() -> None:
    wires: dict[str, int] = dict()
    gates_queue: set[tuple[str | int, ...]] = set()
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            equal_match = re.match(r"^(\w+) -> ([a-z]+)$", line)
            if equal_match is not None:
                f(
                    (EQUAL, equal_match.group(1), equal_match.group(2)),
                    wires,
                    gates_queue,
                )
                continue
            and_match = re.match(r"^(\w+) AND (\w+) -> ([a-z]+)$", line)
            if and_match is not None:
                f(
                    (
                        AND,
                        and_match.group(1),
                        and_match.group(2),
                        and_match.group(3),
                    ),
                    wires,
                    gates_queue,
                )
                continue
            or_match = re.match(r"^(\w+) OR (\w+) -> (\w+)$", line)
            if or_match is not None:
                f(
                    (
                        OR,
                        or_match.group(1),
                        or_match.group(2),
                        or_match.group(3),
                    ),
                    wires,
                    gates_queue,
                )
                continue
            lshift_match = re.match(r"^(\w+) LSHIFT (\d+) -> ([a-z]+)$", line)
            if lshift_match is not None:
                f(
                    (
                        LSHIFT,
                        lshift_match.group(1),
                        lshift_match.group(2),
                        lshift_match.group(3),
                    ),
                    wires,
                    gates_queue,
                )
                continue
            rshift_match = re.match(r"^(\w+) RSHIFT (\d+) -> ([a-z]+)$", line)
            if rshift_match is not None:
                f(
                    (
                        RSHIFT,
                        rshift_match.group(1),
                        rshift_match.group(2),
                        rshift_match.group(3),
                    ),
                    wires,
                    gates_queue,
                )
                continue
            not_match = re.match(r"^NOT (\w+) -> ([a-z]+)$", line)
            if not_match is not None:
                f(
                    (NOT, not_match.group(1), not_match.group(2)),
                    wires,
                    gates_queue,
                )
                continue
            print(wires)
            print(line)
            raise NotImplementedError
    print(f"wires = {wires}")
    print(f"gates_queue = {gates_queue}")
    while len(gates_queue) > 0:
        for gate in gates_queue:
            if f(gate, wires, gates_queue):
                gates_queue.remove(gate)
                break
    print(wires[WIRE])


if __name__ == "__main__":
    main()
