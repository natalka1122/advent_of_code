from collections.abc import Callable
import re

FILENAME = "demo.txt"  # expected 5
FILENAME = "input.txt"


def main() -> None:
    def nop(_: int, x: int, index: int) -> tuple[int, int]:
        return (x, index + 1)

    def acc(v: int, x: int, index: int) -> tuple[int, int]:
        return (x + v, index + 1)

    def jmp(v: int, x: int, index: int) -> tuple[int, int]:
        return (x, index + v)

    program: list[tuple[Callable[[int, int, int], tuple[int, int]], int]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"(nop|acc|jmp) (\+?)(\-?)(\d+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            if line_match.group(2) == "+":
                number = int(line_match.group(4))
            elif line_match.group(3) == "-":
                number = -int(line_match.group(4))
            else:
                raise NotImplementedError
            if line_match.group(1) == "nop":
                program.append((nop, number))
            elif line_match.group(1) == "acc":
                program.append((acc, number))
            elif line_match.group(1) == "jmp":
                program.append((jmp, number))
    executed = set()
    index = 0
    x = 0
    while index not in executed:
        executed.add(index)
        x, index = program[index][0](program[index][1], x, index)
        print(f"index = {index} x = {x}")
    print(x)


if __name__ == "__main__":
    main()
