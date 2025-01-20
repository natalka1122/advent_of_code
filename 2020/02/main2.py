import re

FILENAME = "demo.txt"  # expected 1
FILENAME = "input.txt"


def f(count1: int, count2: int, letter: str, line: str) -> bool:
    if line[count1] == letter and line[count2] != letter:
        return True
    if line[count2] == letter and line[count1] != letter:
        return True
    return False


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            if f(
                int(line_match.group(1)) - 1,
                int(line_match.group(2)) - 1,
                line_match.group(3),
                line_match.group(4),
            ):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
