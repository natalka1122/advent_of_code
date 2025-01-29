from functools import reduce

FILENAME = "demo.txt"  # expected 1242
# FILENAME = "input.txt"

ONE = "1"
SIZE = 128
LIST_SIZE = 256
ROUND_COUNT = 64
SIXTEEN = 16
ADD_SEQUENCE = [17, 31, 73, 47, 23]


def f(
    the_list: list[int], current_position: int, length: int, skip_size: int
) -> tuple[list[int], int]:
    if current_position + length <= len(the_list):
        result = (
            the_list[:current_position]
            + the_list[current_position : current_position + length][::-1]
            + the_list[current_position + length :]
        )
    else:
        # lazy option
        result = the_list[current_position:] + the_list[:current_position]
        result = result[:length][::-1] + result[length:]
        result = result[-current_position:] + result[:-current_position]
        # extra = current_position + length - len(the_list)
        # result = (
        #     the_list[current_position : current_position + extra][::-1]
        #     + the_list[extra:current_position]
        #     + the_list[:extra][::-1]
        #     + the_list[current_position + extra :][::-1]
        # )
    return result, (current_position + length + skip_size) % len(the_list)


def knot_hash(lengths: list[int]) -> list[bool]:
    sparse_hash: list[int] = [x for x in range(LIST_SIZE)]
    skip_size = 0
    current_position = 0
    for _ in range(ROUND_COUNT):
        for length in lengths + ADD_SEQUENCE:
            sparse_hash, current_position = f(sparse_hash, current_position, length, skip_size)
            skip_size += 1
    dense_hash = []
    for i in range(SIXTEEN):
        dense_hash.append(reduce(lambda x, y: x ^ y, sparse_hash[i * SIXTEEN : (i + 1) * SIXTEEN]))
    result = ""
    for num in dense_hash:
        result += bin(num)[2:].zfill(8)
    if len(result) != SIZE:
        raise NotImplementedError
    return list(map(lambda x: x == ONE, result))


def clean_island(y0: int, x0: int, grid: list[list[bool]]) -> None:
    if not grid[y0][x0]:
        raise NotImplementedError
    Q = {(y0, x0)}
    while len(Q) > 0:
        y,x = Q.pop()
        if not grid[y][x]:
            raise NotImplementedError
        grid[y][x] = False
        if y > 0 and grid[y - 1][x]:
            Q.add((y - 1, x))
        if x > 0 and grid[y][x - 1]:
            Q.add((y, x - 1))
        if y < len(grid) - 1 and grid[y + 1][x]:
            Q.add((y + 1, x))
        if x < len(grid[0]) - 1 and grid[y][x + 1]:
            Q.add((y, x + 1))


def count_islands(grid: list[list[bool]]) -> int:
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]:
                result += 1
                clean_island(y, x, grid)
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
    grid = []
    for i in range(SIZE):
        current_line = f"{line}-{i}"
        grid.append(knot_hash(list(map(ord, current_line))))
    print(count_islands(grid))


if __name__ == "__main__":
    main()
