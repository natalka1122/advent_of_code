FILENAME = "demo.txt"  # expected 11
FILENAME = "demo1.txt"  # expected 6
FILENAME = "input.txt"


def main() -> None:
    result = 0
    groups: set[str] = set()
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                result += len(groups)
                groups = set()
            else:
                groups.update(set(line))
    result += len(groups)
    print(result)


if __name__ == "__main__":
    main()
