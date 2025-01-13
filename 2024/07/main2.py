from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"


def f(left: int, right: list[int]) -> bool:
    print(f"left = {left} right = {right}")
    for n in range(3 ** (len(right) - 1)):
        result = right[0]
        for i in range(len(right) - 1):
            value = (n // (3**i)) % 3
            if value == 0:
                result *= right[i + 1]
            elif value == 1:
                result += right[i + 1]
            elif value == 2:
                result = int(str(result) + str(right[i + 1]))
            else:
                raise NotImplementedError
            if result > left:
                break
        if result == left:
            return True
    return False


def main():
    result = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(": ")
            left = int(line[0])
            right = tuple(map(int, line[1].split(" ")))
            if f(left, right):
                result += left
    print(result)


if __name__ == "__main__":
    main()
