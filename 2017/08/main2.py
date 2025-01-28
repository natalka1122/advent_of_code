from collections.abc import Callable
import re

FILENAME = "demo.txt"  # expected 10
# FILENAME = "input.txt"

INC = "inc"
DEC = "dec"

F: dict[str, Callable[[int, int], bool]] = {
    ">": lambda x, y: x > y,
    "<": lambda x, y: x < y,
    ">=": lambda x, y: x >= y,
    "<=": lambda x, y: x <= y,
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y,
}


def main() -> None:
    result = 0
    registers: dict[str, int] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"(\w+) (inc|dec) (-?\d+) if (\w+) (>|<|<=|>=|==|!=) (-?\d+)", line.strip()
            )
            if line_match is None:
                raise NotImplementedError
            a = line_match.group(1)
            b = line_match.group(4)
            change_a = int(line_match.group(3))
            if line_match.group(2) == DEC:
                change_a = -change_a
            elif line_match.group(2) != INC:
                raise NotImplementedError
            compare_b = int(line_match.group(6))
            if line_match.group(1) not in registers:
                registers[line_match.group(1)] = 0
            if line_match.group(4) not in registers:
                registers[line_match.group(4)] = 0
            function = F[line_match.group(5)]
            if function(registers[b], compare_b):
                registers[a] += change_a
            print(line_match.groups())
            result = max(result,max(registers.values()))
    print(registers)
    print(result)


if __name__ == "__main__":
    main()
