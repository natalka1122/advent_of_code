from queue import PriorityQueue

FILENAME = "demo.txt"  # expected 45
FILENAME = "input.txt"

ROCKY = 0
WET = 1
NARROW = 2
BIG_NUMBER = 20183
Y_NUMBER = 16807
X_NUMBER = 48271
START = (0, 0, 1)
FINISH_EQUIPMENT = 1
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def main() -> None:
    depth = None
    target = None
    with open(FILENAME, "r") as file:
        for line in file:
            if line.startswith("depth"):
                depth = int(line.split(" ")[1])
            elif line.startswith("target"):
                line_split = line.split(" ")[1].split(",")
                target = int(line_split[1]), int(line_split[0])
            else:
                raise NotImplementedError
    if depth is None or target is None:
        raise NotImplementedError
    # print(depth, target)
    the_map: list[list[int]] = []
    erosion: list[list[int]] = []
    for y in range(3 * target[0] + 1):
        the_map.append([])
        erosion.append([])
        for x in range(3 * target[1] + 1):
            if y == 0:
                if x == 0:
                    value = 0
                else:
                    value = x * X_NUMBER
            elif x == 0:
                value = y * Y_NUMBER
            elif (y, x) == target:
                value = 0
            else:
                value = erosion[y - 1][x] * erosion[y][x - 1]
            erosion[y].append((value + depth) % BIG_NUMBER)
            the_map[y].append(erosion[y][x] % 3)
        # print(the_map[y])
    start = START
    finish = target[0], target[1], FINISH_EQUIPMENT
    Q: PriorityQueue[tuple[int, tuple[int, int, int]]] = PriorityQueue()
    Q.put_nowait((0, start))
    visited = {start}
    while not Q.empty():
        path, node = Q.get_nowait()
        # print(f"path = {path} node = {node}", end=" ")
        if node == finish:
            # print()
            print(path)
            break
        y, x, equip = node
        # Option 1: Change equipment
        new_equipment = 3 - equip - the_map[y][x]
        new_node = (y, x, new_equipment)
        if new_node not in visited:
            visited.add(new_node)
            Q.put_nowait((path + 7, new_node))
            # print((path + 7, new_node), end=" ")
        # Option 2: Go neighbors
        for dy, dx in DIRECTIONS:
            y1 = y + dy
            x1 = x + dx
            if 0 <= y1 < len(the_map) and 0 <= x1 < len(the_map[0]) and the_map[y1][x1] != equip:
                new_node = (y1, x1, equip)
                if new_node not in visited:
                    visited.add(new_node)
                    Q.put_nowait((path + 1, new_node))
                    # print((path + 1, new_node), end=" ")
        # print()


if __name__ == "__main__":
    main()
