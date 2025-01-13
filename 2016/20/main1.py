FILENAME, MAX = "demo.txt", 9  # expected 3
FILENAME, MAX = "input.txt", 4294967295


def main() -> None:
    pairs_set: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            pairs_set.add(tuple(map(int, line.split("-"))))
    pairs = sorted(pairs_set)
    print(pairs)
    if pairs[0][0] > 0:
        print(0)
        return
    index = 0
    current = 0
    while True:
        if current < pairs[index][0]:
            print(current)
            return
        current = max(current, pairs[index][1] + 1)
        index += 1


if __name__ == "__main__":
    main()
