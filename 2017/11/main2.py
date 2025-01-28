FILENAME = "demo.txt"  # expected ?
FILENAME = "input.txt"


def calc_dist(coord: tuple[int, int]) -> int:
    result = 0
    while coord[1] > 0 and coord[0] > 0:
        coord = coord[0] - 1, coord[1] - 1
        result += 1
    while coord[1] < 0 and coord[0] < 0:
        coord = coord[0] + 1, coord[1] + 1
        result += 1
    while coord[1] < 0 and coord[0] > 0:
        coord = coord[0] - 1, coord[1] + 1
        result += 1
    while coord[1] > 0 and coord[0] < 0:
        coord = coord[0] + 1, coord[1] - 1
        result += 1
    if coord[1] == 0:
        return result + abs(coord[0]) // 2
    if coord[0] == 0:
        return result + abs(coord[1])
    raise NotImplementedError


def f(line: list[str]) -> int:
    result = 0
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
        result = max(result, calc_dist(current))
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip().split(",")))


if __name__ == "__main__":
    main()
