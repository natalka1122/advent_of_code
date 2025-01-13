FILENAME = "demo.txt"  # expected 42
FILENAME = "input.txt"
A = "a"
B = "b"
C = "c"
D = "d"
CPY = "cpy"
INC = "inc"
DEC = "dec"
JNZ = "jnz"


def main() -> None:
    program: list[list[str | int]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            line_split = list(
                map(
                    lambda x: int(x) if x.isdigit() or x[1:].isdigit() else x,
                    line.strip().split(" "),
                )
            )
            program.append(line_split)
    print(program)
    a, b, c, d = 0, 0, 0, 0
    index = 0
    while 0 <= index < len(program):
        current = program[index]
        if current[0] == CPY:
            if current[1] == A:
                value = a
            elif current[1] == B:
                value = b
            elif current[1] == C:
                value = c
            elif current[1] == D:
                value = d
            elif isinstance(current[1], int):
                value = current[1]
            else:
                raise NotImplementedError
            if current[2] == A:
                a = value
            elif current[2] == B:
                b = value
            elif current[2] == C:
                c = value
            elif current[2] == D:
                d = value
            else:
                raise NotImplementedError
            index += 1
        elif current[0] == INC:
            if current[1] == A:
                a += 1
            elif current[1] == B:
                b += 1
            elif current[1] == C:
                c += 1
            elif current[1] == D:
                d += 1
            else:
                raise NotImplementedError
            index += 1
        elif current[0] == DEC:
            if current[1] == A:
                a -= 1
            elif current[1] == B:
                b -= 1
            elif current[1] == C:
                c -= 1
            elif current[1] == D:
                d -= 1
            else:
                raise NotImplementedError
            index += 1
        elif current[0] == JNZ:
            if current[1] == A:
                value = a
            elif current[1] == B:
                value = b
            elif current[1] == C:
                value = c
            elif current[1] == D:
                value = d
            elif isinstance(current[1], int):
                value = current[1]
            else:
                raise NotImplementedError
            if value == 0:
                index += 1
            elif isinstance(current[2], int):
                index += current[2]
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError
    print(f"a = {a}")


if __name__ == "__main__":
    main()
