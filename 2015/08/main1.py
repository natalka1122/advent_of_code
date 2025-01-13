import re

FILENAME = "demo.txt"  # expected 12
FILENAME = "input.txt"


def f(line: str) -> int:
    result = ""
    index = 1
    while index < len(line) - 1:
        if re.match(r"\\x[0-9a-f]{2}", line[index : index + 4]):
            result += chr(int(line[index + 2 : index + 4], 16))
            index += 4
        elif re.match(r'\\\\|\\"', line[index : index + 2]):
            result += line[index + 1]
            index += 2
        else:
            result += line[index]
            index += 1
    print(f"line = {line}, result = {result}")
    return len(line) - len(result)


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(line.strip())
    print(result)


if __name__ == "__main__":
    main()
