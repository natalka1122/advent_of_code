FILENAME = "demo1.txt"  # expected 4
FILENAME = "input.txt"

SND = "snd"
SET = "set"
ADD = "add"
MUL = "mul"
MOD = "mod"
RCV = "rcv"
JGZ = "jgz"


def is_number(n: str) -> bool:
    return n.lstrip("-").isdigit()


def main() -> None:
    result = 0
    registers: dict[str, int] = dict()
    program: list[list[str]] = []
    with open(FILENAME, "r") as file:
        for line_ in file:
            program.append(line_.strip().split(" "))
    index = 0
    while 0 <= index < len(program):
        line = program[index]
        if line[0] == SND:
            result = registers[line[1]]
        elif line[0] == SET:
            if is_number(line[2].lstrip("-")):
                b = int(line[2])
            else:
                if line[2] not in registers:
                    registers[line[2]] = 0
                b = registers[line[2]]
            registers[line[1]] = b
        elif line[0] == ADD:
            if line[1] not in registers:
                registers[line[1]] = 0
            if is_number(line[2]):
                b = int(line[2])
            else:
                if line[2] not in registers:
                    registers[line[2]] = 0
                b = registers[line[2]]
            registers[line[1]] += b
        elif line[0] == MUL:
            if line[1] not in registers:
                registers[line[1]] = 0
            if is_number(line[2]):
                b = int(line[2])
            else:
                if line[2] not in registers:
                    registers[line[2]] = 0
                b = registers[line[2]]
            registers[line[1]] *= b
        elif line[0] == MOD:
            if line[1] not in registers:
                registers[line[1]] = 0
            if is_number(line[2]):
                b = int(line[2])
            else:
                if line[2] not in registers:
                    registers[line[2]] = 0
                b = registers[line[2]]
            registers[line[1]] = registers[line[1]] % b
        elif line[0] == RCV:
            if line[1] not in registers:
                registers[line[1]] = 0
            if registers[line[1]] != 0:
                break
        elif line[0] == JGZ:
            if line[1] not in registers:
                registers[line[1]] = 0
            if registers[line[1]] > 0:
                if is_number(line[2]):
                    b = int(line[2])
                else:
                    if line[2] not in registers:
                        registers[line[2]] = 0
                    b = registers[line[2]]
                index += b - 1
        else:
            print(line)
            raise NotImplementedError
        index += 1
    print(result)


if __name__ == "__main__":
    main()
