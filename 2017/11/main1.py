FILENAME = "demo.txt"  # expected 3 0 2 3
FILENAME = "input.txt"


def f(line: list[str]) -> int:
    current = (0, 0)
    for symbol in line:
        if symbol == "n":
            current = current[0] + 2, current[1]
        elif symbol == "s":
            current = current[0] - 2, current[1]
        elif symbol == "ne":
            current = current[0] + 1, current[1] + 1
        elif symbol == "nw":
            current = current[0] + 1, current[1] - 1
        elif symbol == "se":
            current = current[0] - 1, current[1] + 1
        elif symbol == "sw":
            current = current[0] - 1, current[1] - 1
        else:
            print(f"symbol = {symbol}")
            raise NotImplementedError
    # print(current)
    result = 0
    while current[1] > 0 and current[0] > 0:
        current = current[0] - 1, current[1] - 1
        result += 1
    while current[1] < 0 and current[0] < 0:
        current = current[0] + 1, current[1] + 1
        result += 1
    while current[1] < 0 and current[0] > 0:
        current = current[0] - 1, current[1] + 1
        result += 1
    while current[1] > 0 and current[0] < 0:
        current = current[0] + 1, current[1] - 1
        result += 1
    if current[1] == 0:
        return result + abs(current[0]) // 2
    if current[0] == 0:
        return result + abs(current[1])
    raise NotImplementedError


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip().split(",")))


if __name__ == "__main__":
    main()
