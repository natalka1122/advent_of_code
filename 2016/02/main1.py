FILENAME = "demo.txt"  # expected 1985
FILENAME = "input.txt"
L = "L"
R = "R"
D = "D"
U = "U"
DIRECTION = {L: (0, 1), D: (-1, 0), R: (0, -1), U: (1, 0)}
KEYPAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def f(line: str, position: tuple[int, int]) -> tuple[int, int]:
    for symbol in line:
        if symbol == L:
            if position[1] != 0:
                position = position[0], position[1] - 1
        elif symbol == R:
            if position[1] != len(KEYPAD[0]) - 1:
                position = position[0], position[1] + 1
        elif symbol == U:
            if position[0] != 0:
                position = position[0] - 1, position[1]
        elif symbol == D:
            if position[0] != len(KEYPAD) - 1:
                position = position[0] + 1, position[1]
        else:
            print(f"symbol = {symbol}")
            raise NotImplementedError
        # print(f"position = {position}")
        # print(f"keypad = {KEYPAD[position[0]][position[1]]}")
    return position


def main() -> None:
    current = 1, 1
    with open(FILENAME, "r") as file:
        for line in file:
            current = f(line.strip(), current)
            print(KEYPAD[current[0]][current[1]], end="")
    print()


if __name__ == "__main__":
    main()
