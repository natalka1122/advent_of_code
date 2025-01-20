FILENAME = "input.txt"


def f(line: str) -> int:
    a = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    b = int(line[7:].replace("L", "0").replace("R", "1"), 2)
    return 8 * a + b


def main() -> None:
    occupiued = set()
    with open(FILENAME, "r") as file:
        for line in file:
            occupiued.add(f(line.strip()))
    for item in occupiued:
        if item + 1 not in occupiued and item + 2 in occupiued:
            print(item + 1)
            break


if __name__ == "__main__":
    main()
