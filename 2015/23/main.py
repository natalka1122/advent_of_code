from __future__ import annotations

FILENAME, TARGET = "input.txt", "b"
A = "a"
B = "b"


def main() -> None:
    instuctions = []
    with open(FILENAME, "r") as file:
        for line in file:
            instuctions.append(line.strip().split(" ", 1))
    print(instuctions)
    a, b = 1, 0
    index = 0
    while 0 <= index < len(instuctions):
        c1, c2 = instuctions[index]
        if c1 == "hlf":
            if c2 == A:
                a = a // 2
            elif c2 == B:
                b = b // 2
            else:
                raise NotImplementedError
            index += 1
        elif c1 == "tpl":
            if c2 == A:
                a = a * 3
            elif c2 == B:
                b = b * 3
            else:
                raise NotImplementedError
            index += 1
        elif c1 == "inc":
            if c2 == A:
                a = a + 1
            elif c2 == B:
                b = b + 1
            else:
                raise NotImplementedError
            index += 1
        elif c1 == "jmp":
            index += int(c2)
        elif c1 == "jie":
            r, offset = c2.split(", ")
            if r == A:
                if a % 2 == 0:
                    index += int(offset)
                else:
                    index += 1
            elif r == B:
                if b % 2 == 0:
                    index += int(offset)
                else:
                    index += 1
            else:
                raise NotImplementedError
        elif c1 == "jio":
            r, offset = c2.split(", ")
            if r == A:
                if a == 1:
                    index += int(offset)
                else:
                    index += 1
            elif r == B:
                if b == 1:
                    index += int(offset)
                else:
                    index += 1
            else:
                raise NotImplementedError
        else:
            print(f"c1 = {c1} c2 = {c2}")
            raise NotImplementedError
        print(f"a = {a} b = {b}")


if __name__ == "__main__":
    main()
