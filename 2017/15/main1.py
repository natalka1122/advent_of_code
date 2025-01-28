from collections.abc import Callable

FILENAME = "demo.txt"  # expected 588
FILENAME = "input.txt"

GEN_A = 16807
GEN_B = 48271
REMINDER = 2147483647
INSPECT_NUM = 40000000
BIT_MASK = 0xFFFF
F_A: Callable[[int], int] = lambda x: (x * GEN_A) % REMINDER
F_B: Callable[[int], int] = lambda x: (x * GEN_B) % REMINDER


def main() -> None:
    a = None
    b = None
    with open(FILENAME, "r") as file:
        for line in file:
            if "A" in line:
                a = int(line.split(" ")[-1])
            elif "B" in line:
                b = int(line.split(" ")[-1])
            else:
                raise NotImplementedError
    if a is None or b is None:
        raise NotImplementedError
    result = 0
    for _ in range(INSPECT_NUM):
        a = F_A(a)
        b = F_B(b)
        if (a & BIT_MASK) == (b & BIT_MASK):
            result += 1
    print(result)


if __name__ == "__main__":
    main()
