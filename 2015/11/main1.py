import re

# FILENAME = "demo.txt"
FILENAME = "input.txt"


def plus_one(line: str) -> str:
    if line[-1] == "z":
        return plus_one(line[:-1]) + "a"
    return line[:-1] + chr(ord(line[-1]) + 1)


def check_result(line: str) -> bool:
    # case 2
    if "i" in line or "o" in line or "l" in line:
        return False
    # case 3
    if re.search(r"(\w)\1.*(\w)\2", line) is None:
        return False
    # case 1
    for i in range(len(line)-3):
        if ord(line[i+1])-ord(line[i]) == 1 and ord(line[i+2])-ord(line[i+1]) == 1:
            return True
    return False


def f(line: str) -> str:
    result = plus_one(line)
    while not check_result(result):
        result = plus_one(result)
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
