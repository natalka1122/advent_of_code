from collections.abc import Callable

FILENAME = "demo.txt"  # expected 273
# FILENAME = "input.txt"

TILE = "Tile"
ZERO = "."
ONE = "#"
DIRECTIONS2D: dict[tuple[int, int], Callable[[list[str]], str]] = {
    (-1, 0): lambda x: x[0],
    (1, 0): lambda x: "".join(map(lambda y: y[0], x)),
    (0, -1): lambda x: x[-1],
    (0, 1): lambda x: "".join(map(lambda y: y[-1], x)),
}
# ROTATE = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
FLIP = {
    (-1, 0, 1): ((-1, 0, 0), -1),
    (0, -1, 1): ((0, -1, 0), -1),
    (1, 0, 1): ((0, 1, 0), 1),
    (0, 1, 1): ((1, 0, 0), 1),
}


def calc_borders(tile_map: list[str]) -> dict[tuple[int, int, int], str]:
    borders: dict[tuple[int, int, int], str] = dict()
    for dy, dx in DIRECTIONS2D:
        borders[dy, dx, 0] = DIRECTIONS2D[dy, dx](tile_map)
        # borders[dy, dx, 1] = borders[dy, dx, 0][::-1]
    for key, value in FLIP.items():
        borders[key] = borders[value[0]][:: value[1]]
    return borders


class Tile:
    def __init__(self, index: int, tile_map: list[str]):
        if len(tile_map) != len(tile_map[0]):
            raise NotImplementedError
        self.index = index
        self.d = len(tile_map)
        self.tile_map = tile_map
        self.borders = calc_borders(self.tile_map)
        # for dy, dx in DIRECTIONS2D:
        #     self.borders[dy, dx, 0] = DIRECTIONS2D[dy, dx](self.tile_map)
        #     self.borders[dy, dx, 1] = self.borders[dy, dx, 0][::-1]
        self.flipped = True

    def __repr__(self) -> str:
        borders = dict()
        for flip in [0, 1]:
            for dy, dx in DIRECTIONS2D:
                borders[dy, dx, flip] = self.borders[dy, dx, flip]
        return str(borders)

    def show(self) -> str:
        return "\n".join(self.tile_map).replace("1", "#").replace("0", ".")

    # def check_consistency(self) -> bool:
    #     # if self.flip:
    #     #     return True
    #     for dy, dx in DIRECTIONS2D:
    #         if self.borders[dy, dx, 0] != DIRECTIONS2D[dy, dx](self.tile_map):
    #             print("ERROR")
    #             print(f"dy = {dy} dx = {dx}")
    #             print(f"self.borders = {self.borders}")
    #             print(f"self.borders[dy, dx, 0] = {self.borders[dy, dx, 0]}")
    #             print(
    #                 f"DIRECTIONS2D[dy, dx](self.tile_map) = {DIRECTIONS2D[dy, dx](self.tile_map)}"
    #             )
    #             print(self.show())
    #             raise NotImplementedError
    #         if self.borders[dy, dx, 1] != self.borders[dy, dx, 0][::-1]:
    #             print("ERROR")
    #             print(f"dy = {dy} dx = {dx}")
    #             print(f"self.borders[dy, dx, 0] = {self.borders[dy, dx, 0]}")
    #             print(
    #                 f"DIRECTIONS2D[dy, dx](self.tile_map) = {DIRECTIONS2D[dy, dx](self.tile_map)}"
    #             )
    #             print(self.show())
    #             raise NotImplementedError
    #     return True

    def get_next(self, borders: dict[str, set[tuple[int, tuple[int, int, int]]]]) -> None:
        for key, value in self.borders.items():
            if value not in borders:
                raise NotImplementedError
            if (self.index, key) not in borders[value]:
                raise NotImplementedError
            borders[value].remove(((self.index, key)))
        if self.flipped:
            print("flip")
            self.flip()
        else:
            print("rotate")
            self.rotate()
        self.borders = calc_borders(self.tile_map)  # Yes, I am lazy
        self.flipped = not self.flipped
        for key, value in self.borders.items():
            # print(f"key = {key} value = {value}")
            if value not in borders:
                raise NotImplementedError
            if (self.index, key) in borders[value]:
                raise NotImplementedError
            borders[value].add(((self.index, key)))
        # self.check_consistency()

    def rotate(self) -> None:
        tile_map: list[str] = []
        for x in range(self.d):
            tile_map.append("")
            for y in range(self.d):
                tile_map[-1] += self.tile_map[y][x]
        self.tile_map = tile_map
        # borders: dict[tuple[int, int, int], str] = dict()
        # for flip in [0, 1]:
        #     for dy, dx in ROTATE:
        #         borders[dy, dx, flip] = borders[ROTATE[dy, dx][0], ROTATE[dy, dx][1], flip]
        # self.borders = borders
        # Yes, I am lazy

    def flip(self) -> None:
        tile_map: list[str] = []
        for y in range(self.d):
            tile_map.append("")
            for x in range(self.d):
                tile_map[-1] += self.tile_map[y][self.d - x - 1]
        self.tile_map = tile_map
        # borders = dict()
        # for dy, dx, flip in self.borders:
        #     borders[dy, dx, 1 - flip] = self.borders[dy, dx, flip]
        # self.borders = borders
        # Yes, I am lazy
        # self.borders = calc_borders(self.tile_map)


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
                current_tile.append("".join(map(lambda x: "1" if x == ONE else "0", line.strip())))
    tiles[tile_index] = Tile(tile_index, current_tile)
    # print(tiles)
    borders: dict[str, set[tuple[int, tuple[int, int, int]]]] = dict()
    corner_tiles: list[int] = []
    border_tiles: list[int] = []
    middle_tiles: list[int] = []
    for tile_index, tile in tiles.items():
        for key, value in tile.borders.items():
            if value not in borders:
                borders[value] = set()
            borders[value].add((tile_index, key))
            reverse_value = value[::-1]
            if reverse_value not in borders:
                borders[reverse_value] = set()
    for tile_index, tile in tiles.items():
        empty_b = []
        for dy, dx in DIRECTIONS2D:
            if (
                len(borders[tile.borders[dy, dx, 0]]) == 1
                and len(borders[tile.borders[dy, dx, 1]]) == 1
            ):
                empty_b.append((dy, dx))
        if len(empty_b) == 2:
            print(f"tile_index {tile_index} in the corner {empty_b}")
            corner_tiles.append(tile_index)
        elif len(empty_b) == 1:
            print(f"tile_index {tile_index} is border {empty_b}")
            border_tiles.append(tile_index)
        elif len(empty_b) == 0:
            middle_tiles.append(tile_index)
        else:
            print(f"empty_b = {empty_b}")
            raise NotImplementedError
        print(tile_index, tile)
    for key, value in borders.items():
        print(key, len(value), value)
    # if len(corner_tiles) != 4:
    #     raise NotImplementedError
    print("corner_tiles", len(corner_tiles))
    print("border_tiles", len(border_tiles))
    # print(
    #     list(
    #         map(
    #             lambda x: (borders[tiles[corner_tiles[0]].borders[x]]),
    #             [(-1, 0, 0), (-1, 0, 1), (0, -1, 0), (0, -1, 1)],
    #         )
    #     )
    # )
    for _ in range(10):
        print(tiles[border_tiles[0]].show())
        print(tiles[border_tiles[0]])
        tiles[border_tiles[0]].get_next(borders)
        # print(
        #     list(
        #         map(
        #             lambda x: (x[0], len((borders[tiles[corner_tiles[0]].borders[x[0]]]))),
        #             sorted(tiles[corner_tiles[0]].borders.items()),
        #         )
        #     )
        # )
        # print(
        #     list(
        #         map(
        #             lambda x: ( len((borders[tiles[corner_tiles[0]].borders[x]]))),
        #             sorted([(-1, 0, 0), (-1, 0, 1), (0, -1, 0), (0, -1, 1)]),
        #         )
        #     )
        # )

        # print(
        #     corner_tiles[0],
        #     tiles[corner_tiles[0]],
        # )

        # # print(
        # #     list(
        # #         map(
        # #             lambda x: (len((borders[tiles[corner_tiles[0]].borders[x]]))),
        # #             sorted(tiles[corner_tiles[0]].borders.keys()),
        # #         )
        # #     ),
        # # )
        # print(
        #     list(
        #         map(
        #             lambda x: (len((borders[tiles[corner_tiles[0]].borders[x]]))),
        #             [(-1,0,0),(0,-1,0),(1,0,0),(0,1,0)],
        #         )
        #     ),
        # )


if __name__ == "__main__":
    main()
