import re

FILENAME = "demo.txt"  # expected 19
FILENAME = "input.txt"


def f(line: str) -> int:
    result = '"'
    for symbol in line:
        if symbol == '"':
            result += '\\"'
        elif symbol == "\\":
            result += "\\\\"
        else:
            result += symbol
    result += '"'
    print(f"line = {line}, result = {result}")
    return len(result) - len(line)


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(line.strip())
    print(result)


if __name__ == "__main__":
    main()
