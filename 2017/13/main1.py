FILENAME = "demo.txt"  # expected 24
FILENAME = "input.txt"


class Scanner:
    def __init__(self, size: int) -> None:
        self.size = size

    def is_zero(self, time: int) -> bool:
        return time % ((self.size - 1) * 2) == 0


def main() -> None:
    scanners: dict[int, Scanner] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            key, value = line.split(": ")
            scanners[int(key)] = Scanner(int(value))
    result = 0
    for time in sorted(scanners.keys()):
        if scanners[time].is_zero(time):
            result += time * scanners[time].size
    print(result)


if __name__ == "__main__":
    main()
