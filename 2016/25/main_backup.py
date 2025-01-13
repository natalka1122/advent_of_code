from __future__ import annotations

FILENAME = "input.txt"
A = "a"
B = "b"
C = "c"
D = "d"
CPY = "cpy"
INC = "inc"
DEC = "dec"
JNZ = "jnz"
OUT = "out"


def main():
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
    a, b, c, d = 1, 0, 0, 0
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
                print(a,b,c,d)
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
            elif current[2] == A:
                index += a
            elif current[2] == B:
                index += b
            elif current[2] == C:
                index += c
            elif current[2] == D:
                index += d
            elif isinstance(current[2], int):
                index += current[2]
            else:
                print(f"current = {current}")
                raise NotImplementedError
        elif current[0] == OUT:
            if current[1] == A:
                value = a
            elif current[1] == B:
                value = a
            elif current[1] == C:
                value = a
            elif current[1] == D:
                value = d
            elif isinstance(current[1], int):
                value = current[1]
            else:
                raise NotImplementedError
            print(f"OUT {value}")
            index += 1
        else:
            raise NotImplementedError
        # print(a, b, c, d)


if __name__ == "__main__":
    main()
