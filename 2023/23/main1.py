FILENAME = "demo.txt"  # expected 94
FILENAME = "input.txt"

PATH = "."
FOREST = "#"
UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"


def main() -> None:
    start = None
    the_map = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(line.strip())
            if len(the_map) == 1:
                start = (0, the_map[0].index(PATH))
    if start is None:
        raise NotImplementedError
    end = (len(the_map) - 1, the_map[-1].index(PATH))
    print(f"start = {start} end = {end}")
    paths: dict[tuple[int, int], tuple[int, set[tuple[tuple[int, int], ...]]]] = {
        start: (0, {(start,)})
    }
    Q = {start}
    while len(Q) > 0:
        y0, x0 = Q.pop()
        if (y0, x0) not in paths:
            raise NotImplementedError
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            y = y0 + dy
            x = x0 + dx
            if 0 <= y < len(the_map) and 0 <= x < len(the_map[0]):
                if the_map[y][x] == FOREST:
                    continue
                if the_map[y][x] == PATH:
                    if (y, x) in paths:
                        if paths[y, x][0] > paths[y0, x0][0] + 1:
                            continue
                    new_paths: set[tuple[tuple[int, int], ...]] = set()
                    for path in paths[y0, x0][1]:
                        if (y, x) in path:
                            continue
                        new_paths.add(path + ((y, x),))
                    if len(new_paths) > 0:
                        paths[y, x] = (paths[y0, x0][0] + 1, new_paths)
                        if (y, x) not in Q:
                            Q.add((y, x))
                elif the_map[y][x] == DOWN:
                    if the_map[y + 1][x] != PATH:
                        raise NotImplementedError
                    if (y + 1, x) in paths:
                        if paths[y + 1, x][0] > paths[y0, x0][0] + 2:
                            continue
                    new_paths = set()
                    for path in paths[y0, x0][1]:
                        if (y + 1, x) in path:
                            continue
                        new_paths.add(path + ((y + 1, x),))
                    if len(new_paths) > 0:
                        paths[y + 1, x] = (paths[y0, x0][0] + 2, new_paths)
                        if (y + 1, x) not in Q:
                            Q.add((y + 1, x))
                elif the_map[y][x] == RIGHT:
                    if the_map[y][x + 1] != PATH:
                        raise NotImplementedError
                    if (y, x + 1) in paths:
                        if paths[y, x + 1][0] > paths[y0, x0][0] + 2:
                            continue
                    new_paths = set()
                    for path in paths[y0, x0][1]:
                        if (y, x + 1) in path:
                            continue
                        new_paths.add(path + ((y, x + 1),))
                    if len(new_paths) > 0:
                        paths[y, x + 1] = (paths[y0, x0][0] + 2, new_paths)
                        if (y, x + 1) not in Q:
                            Q.add((y, x + 1))
                else:
                    print(the_map[y][x])
                    continue
    # print(paths)
    print(paths[end][0])


if __name__ == "__main__":
    main()
