import re

# FILENAME = "demo1.txt"  # exoected 58
# FILENAME = "demo2.txt"  # exoected 43
FILENAME = "input.txt"


def f(dims: tuple[str, ...]) -> int:
    l, w, h = map(int, dims)
    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line_match = re.match(r"(\d+)x(\d+)x(\d+)", line_.strip())
            if line_match is None:
                raise NotImplementedError
            result += f(line_match.groups())
    print(result)


if __name__ == "__main__":
    main()
