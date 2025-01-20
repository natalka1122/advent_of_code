import re

FILENAME = "demo.txt"  # expected 2
FILENAME = "input.txt"


def f(count1: int, count2: int, letter: str, line: str) -> bool:
    count = line.count(letter)
    return count1 <= count <= count2


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            if f(
                int(line_match.group(1)),
                int(line_match.group(2)),
                line_match.group(3),
                line_match.group(4),
            ):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
