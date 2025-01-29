from collections.abc import Generator

FILENAME = "demo2.txt"  # expected 3
FILENAME = "input.txt"

SND = "snd"
SET = "set"
ADD = "add"
MUL = "mul"
MOD = "mod"
RCV = "rcv"
JGZ = "jgz"
P = "p"


def is_number(n: str) -> bool:
    return n.lstrip("-").isdigit()


def execute(p: int, program: list[list[str]]) -> Generator[list[int], int, None]:
    registers: dict[str, int] = {P: p}
    index = 0
    something_to_yield: list[int] = []
    while 0 <= index < len(program):
        line = program[index]
        if line[0] == SND:
            if is_number(line[1].lstrip("-")):
                b = int(line[1])
            else:
                b = registers[line[1]]
            something_to_yield.append(b)
        elif line[0] == SET:
            if is_number(line[2].lstrip("-")):
                b = int(line[2])
            else:
                b = registers[line[2]]
            registers[line[1]] = b
        elif line[0] == ADD:
            if is_number(line[2]):
                b = int(line[2])
            else:
                b = registers[line[2]]
            registers[line[1]] += b
        elif line[0] == MUL:
            if is_number(line[2]):
                b = int(line[2])
            else:
                b = registers[line[2]]
            registers[line[1]] *= b
        elif line[0] == MOD:
            if is_number(line[2]):
                b = int(line[2])
            else:
                b = registers[line[2]]
            registers[line[1]] = registers[line[1]] % b
        elif line[0] == RCV:
            registers[line[1]] = yield something_to_yield
            something_to_yield = []
        elif line[0] == JGZ:
            if is_number(line[1]):
                a = int(line[1])
            else:
                a = registers[line[1]]
            if a > 0:
                if is_number(line[2]):
                    b = int(line[2])
                else:
                    b = registers[line[2]]
                index += b - 1
        else:
            print(line)
            raise NotImplementedError
        index += 1
    return


def main() -> None:
    result = 0
    program: list[list[str]] = []
    with open(FILENAME, "r") as file:
        for line_ in file:
            program.append(line_.strip().split(" "))
    p0 = execute(0, program)
    p1 = execute(1, program)
    msg_0 = next(p0)
    msg_1 = next(p1)
    result = len(msg_1)
    print(msg_0, msg_1)
    while len(msg_0) > 0 or len(msg_1) > 0:
        if len(msg_1) > 0:
            msg_0.extend(p0.send(msg_1[0]))
            msg_1 = msg_1[1:]
        elif len(msg_0) > 0:
            p1_send = p1.send(msg_0[0])
            result += len(p1_send)
            msg_1.extend(p1_send)
            msg_0 = msg_0[1:]
        # print(f"msg_0 = {msg_0} msg_1 = {msg_1}")
    print(result)


if __name__ == "__main__":
    main()
