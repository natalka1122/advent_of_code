FILENAME = "demo2.txt"  # expected 5 9 18 2018
FILENAME = "demo2_5.txt"  # expected 5
FILENAME = "input.txt"

START_LINE = "37"
TEN = 10


def f(target: str) -> int:
    index1 = 0
    index2 = 1
    line = START_LINE
    while not target in line[-len(target) - 1 :]:
        line += str(int(line[index1]) + int(line[index2]))
        index1 = (index1 + int(line[index1]) + 1) % len(line)
        index2 = (index2 + int(line[index2]) + 1) % len(line)
    return line.index(target)
    return len(line) - len(target)


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
