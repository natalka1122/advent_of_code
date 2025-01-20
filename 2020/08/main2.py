from collections.abc import Callable
import re

FILENAME = "demo.txt"  # expected 8
FILENAME = "input.txt"


def main() -> None:
    def nop(v: int, x: int, index: int) -> tuple[int, int]:
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
    for chg_index in range(len(program)):
        if program[chg_index][0] == acc:
            continue
        executed = set()
        index = 0
        x = 0
        while index not in executed:
            executed.add(index)
            if index == chg_index:
                if program[index][0] == nop:
                    prg = jmp
                elif program[index][0] == jmp:
                    prg = nop
                else:
                    raise NotImplementedError
            else:
                prg = program[index][0]
            x, index = prg(program[index][1], x, index)
            if index >= len(program):
                break
            # print(f"index = {index} x = {x}")
        if index not in executed:
            break
    print(x)


if __name__ == "__main__":
    main()
