import functools

FILENAME = "demo2.txt"  # expected 51314
FILENAME = "input.txt"


@functools.cache
def f(num: int) -> int:
    result = num // 3 - 2
    if result <= 0:
        return 0
    return result + f(result)


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(int(line))
    print(result)


if __name__ == "__main__":
    main()
