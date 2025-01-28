FILENAME = "demo.txt"  # expected 10
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

    sorted_scanners = sorted(scanners.keys())
    result = 0
    is_caught = True
    while is_caught:
        is_caught = False
        for time in sorted_scanners:
            if scanners[time].is_zero(time + result):
                is_caught = True
                break
        if is_caught:
            result += 1
    print(result)


if __name__ == "__main__":
    main()
