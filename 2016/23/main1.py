FILENAME = "demo.txt"  # expected 3
FILENAME = "input.txt"
A = "a"
B = "b"
C = "c"
D = "d"
CPY = "cpy"
INC = "inc"
DEC = "dec"
JNZ = "jnz"
TGL = "tgl"


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
    a, b, c, d = 7, 0, 0, 0
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
        elif current[0] == TGL:
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
            target_index = index + value
            if 0 <= target_index < len(program):
                if len(program[target_index]) == 2:
                    if program[target_index][0] == INC:
                        program[target_index][0] = DEC
                    else:
                        program[target_index][0] = INC
                elif len(program[target_index]) == 3:
                    if program[target_index][0] == JNZ:
                        program[target_index][0] = CPY
                    else:
                        program[target_index][0] = JNZ
                else:
                    raise NotImplementedError
            index += 1
        else:
            raise NotImplementedError
    print(f"a = {a}")


if __name__ == "__main__":
    main()
