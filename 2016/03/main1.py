# FILENAME = "demo.txt"  # expected 0
FILENAME = "input.txt"


def f(sides: list[int]) -> bool:
    if len(sides) != 3:
        raise NotImplementedError
    a, b, c = sides
    return a < b + c and b < a + c and c < a + b


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if f(list(map(int, filter(lambda x: len(x.strip()) > 0, line.split(" "))))):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
