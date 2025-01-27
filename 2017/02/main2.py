FILENAME = "demo2.txt"  # expected 9
FILENAME = "input.txt"


def f(line: list[int]) -> int:
    for i in line:
        for j in line:
            if i <= j:
                continue
            if i % j == 0:
                return i // j
    raise NotImplementedError


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(list(map(int, line.strip().replace("\t", " ").split(" "))))
    print(result)


if __name__ == "__main__":
    main()
