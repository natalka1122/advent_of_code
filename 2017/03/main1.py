FILENAME = "demo.txt"  # expected 0 3 2 31
# FILENAME = "demo1.txt"  # expected ?
FILENAME = "input.txt"


def f(num: int) -> int:
    if num <= 0:
        raise NotImplementedError
    if num == 1:
        return 0
    closest = int(num ** (1 / 2))
    if closest % 2 == 0:
        current_pos = closest // 2, 1 - closest // 2
        dydx = [(0, -1), (-1, 0), (0, 1)]
    else:
        current_pos = -(closest // 2), closest // 2
        dydx = [(0, 1), (1, 0), (0, -1)]
    dydx_index = 0
    current_number = closest * closest
    while current_number != num:
        current_number += 1
        current_pos = current_pos[0] + dydx[dydx_index][0], current_pos[1] + dydx[dydx_index][1]
        if abs(current_pos[0]) + abs(current_pos[1]) == closest:
            dydx_index += 1
    return abs(current_pos[0]) + abs(current_pos[1])


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(int(line)))


if __name__ == "__main__":
    main()
