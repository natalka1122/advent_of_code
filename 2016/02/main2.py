# FILENAME = "demo.txt"  # expected 5DB3
FILENAME = "input.txt"
L = "L"
R = "R"
D = "D"
U = "U"
DIRECTION = {L: (0, 1), D: (-1, 0), R: (0, -1), U: (1, 0)}
KEYPAD = {
    (0, 0): "5",
    (0, 1): "6",
    (0, 2): "7",
    (0, 3): "8",
    (0, 4): "9",
    (-1, 1): "2",
    (-1, 2): "3",
    (-1, 3): "4",
    (-2, 2): "1",
    (1, 1): "A",
    (1, 2): "B",
    (1, 3): "C",
    (2, 2): "D",
}


def f(line: str, position: tuple[int, int]) -> tuple[int, int]:
    for symbol in line:
        if symbol == L:
            new_position = position[0], position[1] - 1
        elif symbol == R:
            new_position = position[0], position[1] + 1
        elif symbol == U:
            new_position = position[0] - 1, position[1]
        elif symbol == D:
            new_position = position[0] + 1, position[1]
        else:
            print(f"symbol = {symbol}")
            raise NotImplementedError
        if new_position in KEYPAD:
            position = new_position
        # print(f"position = {position}")
        # print(f"keypad = {KEYPAD[position]}")
    return position


def main() -> None:
    current = 1, 1
    with open(FILENAME, "r") as file:
        for line in file:
            current = f(line.strip(), current)
            print(KEYPAD[current], end="")
    print()


if __name__ == "__main__":
    main()
