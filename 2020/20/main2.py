FILENAME = "demo.txt"  # expected 20899048083289
FILENAME = "input.txt"

TILE = "Tile"
ZERO = "."
ONE = "#"


class Tile:
    def __init__(self, tile_map: list[str]):
        self.borders: dict[tuple[int, int, int], str] = {
            (-1, 0, 0): tile_map[0],
            (0, -1, 0): "".join(map(lambda x: x[0], tile_map)),
            (1, 0, 0): tile_map[-1],
            (0, 1, 0): "".join(map(lambda x: x[-1], tile_map)),
            (-1, 0, 1): tile_map[0][::-1],
            (0, -1, 1): "".join(map(lambda x: x[0], tile_map))[::-1],
            (1, 0, 1): tile_map[-1][::-1],
            (0, 1, 1): "".join(map(lambda x: x[-1], tile_map))[::-1],
        }

    def __repr__(self) -> str:
        return str(self.borders)


def main() -> None:
    tiles: dict[int, Tile] = dict()
    tile_index = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                tiles[tile_index] = Tile(current_tile)
            elif line.startswith(TILE):
                tile_index = int(line[5:9])
                current_tile: list[str] = []
            else:
                current_tile.append("".join(map(lambda x: "1" if x == ONE else "0", line.strip())))
    tiles[tile_index] = Tile(current_tile)
    # print(tiles)
    borders: dict[str, set[tuple[int, tuple[int, int, int]]]] = dict()
    for tile_index in tiles:
        for key, value in tiles[tile_index].borders.items():
            if value not in borders:
                borders[value] = set()
            borders[value].add((tile_index, key))
    # for b in borders.values():
    #     print(len(b), b)
    corners: list[int] = []
    for tile_index, tile in tiles.items():
        empty_b = 0
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (
                len(borders[tile.borders[dy, dx, 0]]) == 1
                and len(borders[tile.borders[dy, dx, 1]]) == 1
            ):
                empty_b += 1
        if empty_b == 2:
            print(f"tile_index {tile_index} in the corner")
            corners.append(tile_index)
    if len(corners) != 4:
        raise NotImplementedError
    print(corners[0] * corners[1] * corners[2] * corners[3])


if __name__ == "__main__":
    main()
