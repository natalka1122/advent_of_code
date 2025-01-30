FILENAME = "input.txt"

SET = "set"
SUB = "sub"
MUL = "mul"
JNZ = "jnz"
REGISTERS = "abcdefgh"
A = "a"
H = "h"


def is_number(n: str) -> bool:
    return n.lstrip("-").isdigit()


def main() -> None:
    registers: dict[str, int] = {x: 0 for x in REGISTERS}
    registers[A] = 1
    program: list[list[str]] = []
    with open(FILENAME, "r") as file:
        for line_ in file:
            program.append(line_.strip().split(" "))
    index = 0
    while 0 <= index < len(program):
        line = program[index]
        print(index, " ".join(line), end=" ")
        if line[0] == SET:
            if is_number(line[2].lstrip("-")):
                b = int(line[2])
            else:
                b = registers[line[2]]
            registers[line[1]] = b
        elif line[0] == SUB:
            if is_number(line[2]):
                b = int(line[2])
            else:
                b = registers[line[2]]
            registers[line[1]] -= b
        elif line[0] == MUL:
            if is_number(line[2]):
                b = int(line[2])
            else:
                b = registers[line[2]]
            registers[line[1]] *= b
        elif line[0] == JNZ:
            if is_number(line[1]):
                a = int(line[1])
            else:
                a = registers[line[1]]
            if a != 0:
                if is_number(line[2]):
                    b = int(line[2])
                else:
                    b = registers[line[2]]
                index += b - 1
        else:
            print(line)
            raise NotImplementedError
        print(registers)
        index += 1
    print(registers[H])


if __name__ == "__main__":
    main()
