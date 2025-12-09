# FILENAME = "demo.txt"  # expected 50
FILENAME = "input.txt"


def main() -> None:
    reds: list[tuple[int, int]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            y, x = map(int, line.strip().split(","))
            reds.append((y, x))
    best = 0
    for i in range(len(reds)):
        for j in range(i):
            current = (abs(reds[i][0] - reds[j][0]) + 1) * (abs(reds[i][1] - reds[j][1]) + 1)
            best = max(best, current)
    print(best)


if __name__ == "__main__":
    main()
