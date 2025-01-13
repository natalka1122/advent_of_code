FILENAME, MAX = "demo.txt", 9  # expected 2
FILENAME, MAX = "input.txt", 4294967295


def main() -> None:
    pairs_set: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            pairs_set.add(tuple(map(int, line.split("-"))))
    pairs = sorted(pairs_set)
    print(pairs)
    allowed = 0
    index = 0
    current = 0
    for index in range(len(pairs)):
        if current < pairs[index][0]:
            allowed += pairs[index][0] - current
        current = max(current, pairs[index][1] + 1)
        index += 1
    allowed += MAX - current + 1
    print(allowed)


if __name__ == "__main__":
    main()
