FILENAME, LENGTH = "demo.txt", 20  # expected 01100
FILENAME, LENGTH = "input.txt", 35651584


def checksum(line: str) -> str:
    if len(line) % 2 == 1:
        return line
    result = ""
    for i in range(0, len(line), 2):
        result += "1" if line[i] == line[i + 1] else "0"
    return checksum(result)


def f(line: str) -> str:
    if len(line) > LENGTH:
        return line[:LENGTH]
    result = line + "0" + "".join(map(lambda x: str(1 - int(x)), line[::-1]))
    return f(result)


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(checksum(f(line)))


if __name__ == "__main__":
    main()
