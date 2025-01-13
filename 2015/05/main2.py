import re

# FILENAME = "demo2.txt"  # expected 2
FILENAME = "input.txt"


def is_nice(s: str) -> bool:
    if re.search(r"(\w{2}).*\1", s) is None:
        print(s, "case 1")
        return False
    if re.search(r"(\w).\1", s) is None:
        print(s, "case 2")
        return False
    return True


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if is_nice(line.strip()):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
