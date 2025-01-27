FILENAME = "demo2.txt"  # expected 3
FILENAME = "input.txt"


def f(line: list[str]) -> bool:
    line = list(map(lambda x: "".join(sorted(x)), line))
    return len(set(line)) == len(line)


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if f(line.strip().split(" ")):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
