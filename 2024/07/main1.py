from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"


def f(left: int, right: list[int]) -> bool:
    print(f"left = {left} right = {right}")
    for i in range(2 ** (len(right) - 1)):
        result = right[0]
        string = bin(i)[2:]
        string = "0"*(len(right)-len(string)-1)+string
        for key, value in enumerate(string):
            if value == "0":
                result *= right[key + 1]
            elif value == "1":
                result += right[key + 1]
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
