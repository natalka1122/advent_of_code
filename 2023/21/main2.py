FILENAME, MAX_STEPS = "demo.txt", 6  # expected 16
FILENAME, MAX_STEPS = "demo.txt", 10  # expected 50
FILENAME, MAX_STEPS = "demo.txt", 50  # expected 1594
# FILENAME, MAX_STEPS = "demo.txt", 100  # expected 6536
# FILENAME, MAX_STEPS = "demo.txt", 500  # expected 167004
# FILENAME, MAX_STEPS = "demo.txt", 1000  # expected 668697
# FILENAME, MAX_STEPS = "demo.txt", 5000  # expected 16733044
# FILENAME, MAX_STEPS = "input.txt", 64  # expected 3639
FILENAME, MAX_STEPS = "input.txt", 26501365

START = "S"
ROCK = "#"
EMPTY = "."
DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
Point = tuple[int, int]


class TheMap:
    def __init__(self, items: list[str]) -> None:
        self.height = len(items)
        self.width = len(items[0])
        self.counter: list[dict[Point, set[Point]]] = [dict()]
        self.sum: list[int] = [0]
        for y in range(self.height):
            for x in range(self.width):
                if items[y][x] == ROCK:
                    continue
                if items[y][x] == START:
                    self.counter[0][y, x] = {(0, 0)}
                    self.sum[0] += 1
                elif items[y][x] == EMPTY:
                    self.counter[0][y, x] = set()
                else:
                    raise NotImplementedError

    def show(self, step: int) -> str:
        result = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                if (y, x) in self.counter[step]:
                    line.append(str(self.counter[step][y, x]).ljust(20))
                else:
                    line.append("_".ljust(20))
            result.append("".join(line))
        return "\n".join(result)

    def get_next_step(self) -> None:
        step_index = len(self.sum)
        self.sum.append(0)
        self.counter.append(dict())
        for y0 in range(self.height):
            for x0 in range(self.width):
                if (y0, x0) not in self.counter[step_index - 1]:
                    continue
                self.counter[step_index][y0, x0] = set()
                for dy, dx in DIRECTIONS:
                    y = y0 + dy
                    x = x0 + dx
                    if (y % self.height, x % self.width) not in self.counter[
                        step_index - 1
                    ]:
                        continue
                    if 0 <= y < self.height and 0 <= x < self.width:
                        for key in self.counter[step_index - 1][y, x]:
                            self.counter[step_index][y0, x0].add(key)
                    else:
                        for y1, x1 in self.counter[step_index - 1][
                            y % self.height, x % self.width
                        ]:
                            self.counter[step_index][y0, x0].add(
                                (y1 + y // self.height, x1 + x // self.width)
                            )
                self.sum[step_index] += len(self.counter[step_index][y0, x0])


def calculate(x: list[int], y: list[int], target: int) -> int:
    # Unpack x and y values
    x1, x2, x3 = x
    y1, y2, y3 = y
    # Solved by ChatGPT
    denominator = (
        x1**2 * x2 - x1**2 * x3 - x1 * x2**2 + x1 * x3**2 + x2**2 * x3 - x2 * x3**2
    )
    a = -x1 * y2 + x1 * y3 + x2 * y1 - x2 * y3 - x3 * y1 + x3 * y2
    b = x1**2 * y2 - x1**2 * y3 - x2**2 * y1 + x2**2 * y3 + x3**2 * y1 - x3**2 * y2
    c = (
        x1**2 * x2 * y3
        - x1**2 * x3 * y2
        - x1 * x2**2 * y3
        + x1 * x3**2 * y2
        + x2**2 * x3 * y1
        - x2 * x3**2 * y1
    )
    if denominator < 0:
        a, b, c, denominator - a, -b, -c, -denominator
    t = a * target * target + b * target + c
    if t % denominator != 0:
        raise NotImplementedError
    return t // denominator


def main() -> None:
    the_map = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(line.strip())
    cell_map = TheMap(the_map)
    x = []
    y = []
    for step in range(2 * cell_map.height + MAX_STEPS % cell_map.height):
        cell_map.get_next_step()
        if (step + 1) % cell_map.height == MAX_STEPS % cell_map.height:
            # print(f"step {step+1}")
            # print(cell_map.sum[step + 1])
            if len(x) < 3:
                x.append(step + 1)
                y.append(cell_map.sum[step + 1])

    print(calculate(x, y, MAX_STEPS))


if __name__ == "__main__":
    main()
