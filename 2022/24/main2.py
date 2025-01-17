FILENAME = "demo.txt"  # expected 54
# FILENAME = "input.txt"

WALL = "#"


class Blizzard:
    def __init__(self, y: int, x: int, direction: int, limit: int) -> None:
        self.y = y
        self.x = x
        self.direction = direction
        self.limit = limit

    def next(self) -> tuple[int, int]:
        if self.direction == 0:
            self.x = (self.x + 1) % self.limit
        elif self.direction == 1:
            self.x = (self.x - 1) % self.limit
        elif self.direction == 2:
            self.y = (self.y - 1) % self.limit
        elif self.direction == 3:
            self.y = (self.y + 1) % self.limit
        else:
            raise NotImplementedError
        return self.y, self.x


class TheMap:
    def __init__(self, map_str: list[str]) -> None:
        if any(map(lambda x: x != WALL, map_str[0][0] + map_str[0][2:])):
            raise NotImplementedError
        if any(map(lambda x: x != WALL, map_str[-1][:-3] + map_str[0][-1])):
            raise NotImplementedError
        self.height = len(map_str) - 2
        self.width = len(map_str[0]) - 2
        self.start = (0, 0)
        self.end = self.height + 1, self.width - 1
        self.blizzards: set[Blizzard] = set()
        for y, line in enumerate(map_str[1:-1]):
            if line[0] != WALL or line[-1] != WALL:
                raise NotImplementedError
            for x, symbol in enumerate(line[1:-1]):
                if symbol == ">":
                    self.blizzards.add(Blizzard(y, x, 0, self.width))
                elif symbol == "<":
                    self.blizzards.add(Blizzard(y, x, 1, self.width))
                elif symbol == "^":
                    self.blizzards.add(Blizzard(y, x, 2, self.height))
                elif symbol == "v":
                    self.blizzards.add(Blizzard(y, x, 3, self.height))
                elif symbol != ".":
                    raise NotImplementedError

    def get_next_map(self) -> list[list[bool]]:
        blizzards_set = set()
        for blizzard in self.blizzards:
            blizzards_set.add(blizzard.next())
        result: list[list[bool]] = [[True]]
        for x in range(1, self.width):
            result[0].append(False)
        for y in range(self.height):
            result.append([])
            for x in range(self.width):
                result[-1].append((y, x) not in blizzards_set)
        result.append([])
        for x in range(self.width - 1):
            result[-1].append(False)
        result[-1].append(True)
        return result


def main() -> None:
    map_str: list[str] = []
    with open(FILENAME, "r") as file:
        for line in file:
            map_str.append(line.strip())
    the_map = TheMap(map_str)
    step = 0
    Q: set[tuple[int, int]] = {the_map.start}
    while len(Q) > 0 and the_map.end not in Q:
        next_Q: set[tuple[int, int]] = set()
        next_map = the_map.get_next_map()
        for y0, x0 in Q:
            for dy, dx in [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]:
                y = y0 + dy
                if y < 0 or y >= the_map.height + 2:
                    continue
                x = x0 + dx
                if x < 0 or x >= the_map.width:
                    continue
                if next_map[y][x]:
                    next_Q.add((y, x))
        Q = next_Q
        step += 1
    print(f"Stage 1: {step}")
    # the_map.get_next_map()
    # step += 1
    # the_map.get_next_map()
    # step += 1
    # the_map.get_next_map()
    # step += 1
    Q = {the_map.end}
    while len(Q) > 0 and the_map.start not in Q:
        next_Q = set()
        next_map = the_map.get_next_map()
        for y0, x0 in Q:
            for dy, dx in [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]:
                y = y0 + dy
                if y < -1 or y >= the_map.height + 2:
                    continue
                x = x0 + dx
                if x < 0 or x >= the_map.width:
                    continue
                if next_map[y][x]:
                    next_Q.add((y, x))
        Q = next_Q
        step += 1
    # the_map.get_next_map()
    print(f"Stage 2: {step}")
    Q = {the_map.start}
    while len(Q) > 0 and the_map.end not in Q:
        next_Q = set()
        next_map = the_map.get_next_map()
        for y0, x0 in Q:
            for dy, dx in [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]:
                y = y0 + dy
                if y < 0 or y >= the_map.height + 2:
                    continue
                x = x0 + dx
                if x < 0 or x >= the_map.width:
                    continue
                if next_map[y][x]:
                    next_Q.add((y, x))
        Q = next_Q
        step += 1
    print(f"Stage 3: {step}")


if __name__ == "__main__":
    main()
