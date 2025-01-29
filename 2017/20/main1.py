import re

FILENAME = "demo1.txt"  # expected 0
FILENAME = "input.txt"


def calc_dist(x: int, y: int, z: int) -> int:
    return x * x + y * y + z * z


def main() -> None:
    index = 0
    best_index = 0
    best_dist = None
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"p=< ?(-?\d+),(-?\d+),(-?\d+)>, v=< ?(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>",
                line,
            )
            if line_match is None:
                raise NotImplementedError
            print(line_match.groups())
            dist = (
                calc_dist(
                    int(line_match.group(7)), int(line_match.group(8)), int(line_match.group(9))
                ),
                calc_dist(
                    int(line_match.group(4)), int(line_match.group(5)), int(line_match.group(6))
                ),
            )
            if best_dist is None or dist < best_dist:
                best_dist = dist
                best_index = index
            elif dist == best_dist:
                raise NotImplementedError
            print(dist, best_dist, best_index)
            index += 1
    print(best_index)


if __name__ == "__main__":
    main()
