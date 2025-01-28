FILENAME = "demo1.txt"  # expected ?
FILENAME = "input.txt"


def mh_dist(coord: tuple[int, int]) -> int:
    return abs(coord[0]) + abs(coord[1])


def max_dist(coord: tuple[int, int]) -> int:
    return max(abs(coord[0]), abs(coord[1]))


def get_sum(coord: tuple[int, int], field: dict[tuple[int, int], int]) -> int:
    result = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            if (coord[0] + dy, coord[1] + dx) in field:
                result += field[coord[0] + dy, coord[1] + dx]
    return result


def get_next(field: dict[tuple[int, int], int], coord: tuple[int, int]) -> tuple[int, int]:
    current_max_dist = max_dist(coord)
    for dy, dx in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        go_there = coord[0] + dy, coord[1] + dx
        if go_there not in field:
            if max_dist(go_there) == current_max_dist:
                field[go_there] = get_sum(go_there, field)
                return go_there
    for dy, dx in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        go_there = coord[0] + dy, coord[1] + dx
        if go_there not in field:
            field[go_there] = get_sum(go_there, field)
            return go_there
    raise NotImplementedError


def main() -> None:
    field: dict[tuple[int, int], int] = {(0, 0): 1}
    with open(FILENAME, "r") as file:
        for line in file:
            target_value = int(line)
    coord = (0, 0)
    while field[coord] <= target_value:
        coord = get_next(field, coord)
        print(field)
    print(field[coord])


if __name__ == "__main__":
    main()
