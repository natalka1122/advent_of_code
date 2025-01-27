from collections.abc import Callable

FILENAME = "demo.txt"  # expected 273
# FILENAME = "demo1.txt"
FILENAME = "input.txt"

TILE = "Tile"
ZERO = "."
ONE = "#"
FOUR = 4
DIRECTIONS2D: dict[tuple[int, int], Callable[[list[str]], str]] = {
    (-1, 0): lambda x: x[0],
    (0, -1): lambda x: "".join(map(lambda y: y[0], x)),
    (1, 0): lambda x: x[-1],
    (0, 1): lambda x: "".join(map(lambda y: y[-1], x)),
}
SEA_MONSTER = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]


def calc_borders(tile_map: list[str]) -> dict[tuple[int, int], str]:
    borders: dict[tuple[int, int], str] = dict()
    for dy, dx in DIRECTIONS2D:
        borders[dy, dx] = DIRECTIONS2D[dy, dx](tile_map)
    return borders


def rotate(tile_map: list[str]) -> list[str]:
    result: list[str] = []
    size = len(tile_map)
    if size != len(tile_map[0]):
        raise NotImplementedError
    for x in range(size):
        result.append("")
        for y in range(size):
            result[-1] += tile_map[y][x]
    return result


def flip(tile_map: list[str]) -> list[str]:
    result: list[str] = []
    size = len(tile_map)
    if size != len(tile_map[0]):
        raise NotImplementedError
    for y in range(size):
        result.append("")
        for x in range(size):
            result[-1] += tile_map[y][size - x - 1]
    return result


class Tile:
    def __init__(self, index: int, tile_map: list[str]):
        if len(tile_map) != len(tile_map[0]):
            raise NotImplementedError
        self.index = index
        self.d = len(tile_map)
        self.tile_map = [tile_map]
        for i in range(FOUR):
            self.tile_map.append(flip(self.tile_map[-1]))
            if i < FOUR - 1:
                self.tile_map.append(rotate(self.tile_map[-1]))
        self.borders = list(map(calc_borders, self.tile_map))

    def __repr__(self) -> str:
        return str(self.borders)

    def show(self, index: int) -> str:
        return "\n".join(self.tile_map[index])


def find_monster(picture: list[str]) -> int:
    result = 0
    for y0 in range(len(picture) - len(SEA_MONSTER)):
        for x0 in range(len(picture[0]) - len(SEA_MONSTER[0])):
            is_found = True
            for y in range(len(SEA_MONSTER)):
                for x in range(len(SEA_MONSTER[0])):
                    if SEA_MONSTER[y][x] == ONE:
                        if picture[y0 + y][x0 + x] != ONE:
                            is_found = False
                            break
                if not is_found:
                    break
            if is_found:
                # print(f"FOUND {y0} {x0}")
                result += 1
    return result


def main() -> None:
    tiles: dict[int, Tile] = dict()
    tile_index = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                tiles[tile_index] = Tile(tile_index, current_tile)
            elif line.startswith(TILE):
                tile_index = int(line[5:9])
                current_tile: list[str] = []
            else:
                current_tile.append(line.strip())
    tiles[tile_index] = Tile(tile_index, current_tile)
    borders: dict[str, set[tuple[int, tuple[int, int], int]]] = dict()
    corner_tiles: list[int] = []
    border_tiles: list[int] = []
    middle_tiles: list[int] = []
    for tile_index, tile in tiles.items():
        for index in range(len(tile.borders)):
            for key, value in tile.borders[index].items():
                if value not in borders:
                    borders[value] = set()
                borders[value].add((tile_index, key, index))
    for tile_index, tile in tiles.items():
        dead_ends = set()
        paired_ends = set()
        for index in range(len(tile.borders)):
            for key, value in tile.borders[index].items():
                current_len = len(set(map(lambda x: x[0], borders[value])))
                if current_len == 1:
                    if value in paired_ends:
                        raise NotImplementedError
                    dead_ends.add(value)
                elif current_len == 2:
                    if value in dead_ends:
                        raise NotImplementedError
                    paired_ends.add(value)
                else:
                    raise NotImplementedError
        if len(dead_ends) == 4:
            print(f"tile_index {tile_index} in the corner {dead_ends}")
            corner_tiles.append(tile_index)
        elif len(dead_ends) == 2:
            print(f"tile_index {tile_index} is border {dead_ends}")
            border_tiles.append(tile_index)
        elif len(dead_ends) == 0:
            middle_tiles.append(tile_index)
        else:
            print(len(dead_ends))
            corner_tiles.append(tile_index)
            raise NotImplementedError
    # for border_name, border_positions in borders.items():
    #     print(border_name, len(border_positions), border_positions)
    # print("corner_tiles", len(corner_tiles), corner_tiles)
    # print("border_tiles", len(border_tiles), border_tiles)
    # Gather first row
    # Chose left-top corner randomly
    left_top_corner = corner_tiles.pop()
    for index in range(len(tiles[left_top_corner].borders)):
        left_border = set(
            map(lambda x: x[0], borders[tiles[left_top_corner].borders[index][-1, 0]])
        )
        top_border = set(map(lambda x: x[0], borders[tiles[left_top_corner].borders[index][0, -1]]))
        if len(left_border) == 1 and len(top_border) == 1:
            break
    if len(left_border) != 1 and len(top_border) != 1:
        raise NotImplementedError
    matrix: list[list[tuple[int, int]]] = [[(left_top_corner, index)]]
    # Gather border tiles in first row
    is_found = True
    while is_found:
        is_found = False
        for tile_index in border_tiles:
            for index in range(len(tiles[tile_index].borders)):
                top_border = set(
                    map(lambda x: x[0], borders[tiles[tile_index].borders[index][-1, 0]])
                )
                left_tile_border = tiles[matrix[0][-1][0]].borders[matrix[0][-1][1]][0, 1]
                if (
                    len(top_border) == 1
                    and left_tile_border == tiles[tile_index].borders[index][0, -1]
                ):
                    print("FOUND", tile_index, index)
                    matrix[0].append((tile_index, index))
                    border_tiles.remove(tile_index)
                    is_found = True
                    break
            if is_found:
                break
    print(f"Border tiles in first row done, matrix = {matrix}")
    # Gather top-left corner
    is_found = False
    for tile_index in corner_tiles:
        for index in range(len(tiles[tile_index].borders)):
            right_border = set(map(lambda x: x[0], borders[tiles[tile_index].borders[index][0, 1]]))
            top_border = set(map(lambda x: x[0], borders[tiles[tile_index].borders[index][-1, 0]]))
            left_tile_border = tiles[matrix[0][-1][0]].borders[matrix[0][-1][1]][0, 1]
            if (
                len(right_border) == 1
                and len(top_border) == 1
                and left_tile_border == tiles[tile_index].borders[index][0, -1]
            ):
                print("FOUND", tile_index, index)
                is_found = True
                break
        if is_found:
            break
    if is_found:
        matrix[0].append((tile_index, index))
        corner_tiles.remove(tile_index)
    else:
        raise NotImplementedError
    # First row is done
    print(f"First row is done, matrix = {matrix}")
    print("corner_tiles", len(corner_tiles), corner_tiles)
    print("border_tiles", len(border_tiles), border_tiles)
    # Gather middle rows
    while len(middle_tiles) > 0:
        # Choose first tile in middle row
        is_found = False
        for tile_index in border_tiles:
            for index in range(len(tiles[tile_index].borders)):
                left_border = set(
                    map(lambda x: x[0], borders[tiles[tile_index].borders[index][0, -1]])
                )
                top_tile_border = tiles[matrix[-1][0][0]].borders[matrix[-1][0][1]][1, 0]
                if (
                    len(left_border) == 1
                    and top_tile_border == tiles[tile_index].borders[index][-1, 0]
                ):
                    print("FOUND", tile_index, index)
                    matrix.append([(tile_index, index)])
                    border_tiles.remove(tile_index)
                    is_found = True
                    break
            if is_found:
                break
        if not is_found:
            raise NotImplementedError
        print(f"First tile in the {len(matrix)} row in done, matrix = {matrix}")
        # Gather middle in the middle row
        is_found = True
        while is_found:
            is_found = False
            for tile_index in middle_tiles:
                for index in range(len(tiles[tile_index].borders)):
                    x = len(matrix[-1])
                    top_tile_border = tiles[matrix[-2][x][0]].borders[matrix[-2][x][1]][1, 0]
                    left_tile_border = tiles[matrix[-1][-1][0]].borders[matrix[-1][-1][1]][0, 1]
                    if (
                        top_tile_border == tiles[tile_index].borders[index][-1, 0]
                        and left_tile_border == tiles[tile_index].borders[index][0, -1]
                    ):
                        print("FOUND", tile_index, index)
                        matrix[-1].append((tile_index, index))
                        middle_tiles.remove(tile_index)
                        is_found = True
                        break
                if is_found:
                    break
        print(f"Middle in the {len(matrix)} row in done, matrix = {matrix}")
        # Gather last tile in the middle row
        is_found = False
        for tile_index in border_tiles:
            for index in range(len(tiles[tile_index].borders)):
                x = len(matrix[-1])
                top_tile_border = tiles[matrix[-2][x][0]].borders[matrix[-2][x][1]][1, 0]
                left_tile_border = tiles[matrix[-1][-1][0]].borders[matrix[-1][-1][1]][0, 1]
                right_border = set(
                    map(lambda x: x[0], borders[tiles[tile_index].borders[index][0, 1]])
                )
                if (
                    len(right_border) == 1
                    and top_tile_border == tiles[tile_index].borders[index][-1, 0]
                    and left_tile_border == tiles[tile_index].borders[index][0, -1]
                ):
                    print("FOUND", tile_index, index)
                    matrix[-1].append((tile_index, index))
                    border_tiles.remove(tile_index)
                    is_found = True
                    break
            if is_found:
                break
        print(f"Last tile in the {len(matrix)} row in done, matrix = {matrix}")
    print("corner_tiles", len(corner_tiles), corner_tiles)
    print("border_tiles", len(border_tiles), border_tiles)
    # Gather first tile in the last row
    is_found = False
    for tile_index in corner_tiles:
        for index in range(len(tiles[tile_index].borders)):
            left_border = set(map(lambda x: x[0], borders[tiles[tile_index].borders[index][0, -1]]))
            bottom_border = set(
                map(lambda x: x[0], borders[tiles[tile_index].borders[index][1, 0]])
            )
            top_tile_border = tiles[matrix[-1][0][0]].borders[matrix[-1][0][1]][1, 0]
            if (
                len(left_border) == 1
                and len(bottom_border) == 1
                and top_tile_border == tiles[tile_index].borders[index][-1, 0]
            ):
                matrix.append([(tile_index, index)])
                corner_tiles.remove(tile_index)
                is_found = True
                break
        if is_found:
            break
    if not is_found:
        raise NotImplementedError
    print(f"First tile in the last row in done, matrix = {matrix}")
    while len(border_tiles) > 0:
        is_found = True
        while is_found:
            is_found = False
            for tile_index in border_tiles:
                for index in range(len(tiles[tile_index].borders)):
                    x = len(matrix[-1])
                    top_tile_border = tiles[matrix[-2][x][0]].borders[matrix[-2][x][1]][1, 0]
                    left_tile_border = tiles[matrix[-1][-1][0]].borders[matrix[-1][-1][1]][0, 1]
                    bottom_border = set(
                        map(lambda x: x[0], borders[tiles[tile_index].borders[index][1, 0]])
                    )
                    if (
                        len(bottom_border) == 1
                        and top_tile_border == tiles[tile_index].borders[index][-1, 0]
                        and left_tile_border == tiles[tile_index].borders[index][0, -1]
                    ):
                        print("FOUND", tile_index, index)
                        matrix[-1].append((tile_index, index))
                        border_tiles.remove(tile_index)
                        is_found = True
                        break
                if is_found:
                    break
        if not is_found:
            break
    print(f"Middle tiles in the last row in done, matrix = {matrix}")
    if len(corner_tiles) != 1 or len(border_tiles) != 0 or len(middle_tiles) != 0:
        raise NotImplementedError
    tile_index = corner_tiles.pop()
    is_found = False
    for index in range(len(tiles[tile_index].borders)):
        x = len(matrix[-1])
        top_tile_border = tiles[matrix[-2][x][0]].borders[matrix[-2][x][1]][1, 0]
        left_tile_border = tiles[matrix[-1][-1][0]].borders[matrix[-1][-1][1]][0, 1]
        bottom_border = set(map(lambda x: x[0], borders[tiles[tile_index].borders[index][1, 0]]))
        right_border = set(map(lambda x: x[0], borders[tiles[tile_index].borders[index][0, 1]]))
        if (
            len(bottom_border) == 1
            and len(right_border) == 1
            and top_tile_border == tiles[tile_index].borders[index][-1, 0]
            and left_tile_border == tiles[tile_index].borders[index][0, -1]
        ):
            print("FOUND", tile_index, index)
            matrix[-1].append((tile_index, index))
            is_found = True
            break
    if not is_found:
        raise NotImplementedError
    print(f"Gathered everything matrix = {matrix}")
    picture: list[str] = []
    size = tiles[matrix[0][0][0]].d
    total = 0
    for y0 in range(len(matrix)):
        for y in range(1, size - 1):
            picture.append("")
            for x0 in range(len(matrix[y0])):
                picture[-1] += tiles[matrix[y0][x0][0]].tile_map[matrix[y0][x0][1]][y][1:-1]
            total += picture[-1].count(ONE)
    print("\n".join(picture))
    print(len(picture))
    result = 0
    for i in range(FOUR):
        result = max(result, find_monster(picture))
        picture = flip(picture)
        result = max(result, find_monster(picture))
        if i < FOUR - 1:
            picture = rotate(picture)
    print(result, total, total - result * "".join(SEA_MONSTER).count(ONE))


if __name__ == "__main__":
    main()
