FILENAME = "demo1.txt"  # expected 12
FILENAME = "input.txt"


def check(line: str, count: int) -> bool:
    for symbol in set(line):
        if line.count(symbol) == count:
            return True
    return False


def main() -> None:
    count_2 = 0
    count_3 = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if check(line.strip(), 2):
                count_2 += 1
            if check(line.strip(), 3):
                count_3 += 1
    print(count_2, count_3)
    print(count_2 * count_3)


if __name__ == "__main__":
    main()
