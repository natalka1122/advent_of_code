import functools

# FILENAME = "demo.txt"  # expected 16
# FILENAME = "demo1.txt"  # expected 4
# FILENAME = "demo2.txt"  # expected 6
FILENAME = "input.txt"


@functools.cache
def f(design: str, patterns: tuple[str]) -> int:
    if not design:
        return 1
    result = 0
    for pattern in patterns:
        if design.startswith(pattern):
            result += f(design[len(pattern) :], patterns)
    return result


def main() -> None:
    result: int = 0
    with open(FILENAME, "r") as file:
        patterns = tuple(file.readline().strip().split(", "))
        file.readline()
        for line_ in file:
            line = line_.strip()
            result += f(line, patterns)
    print(result)


if __name__ == "__main__":
    main()
