FILENAME = "demo.txt"  # expect 157
FILENAME = "input.txt"


def f(line: str) -> int:
    p1 = line[: len(line) // 2]
    p2 = line[len(line) // 2 :]
    is_found = False
    for letter in p1:
        if letter in p2:
            is_found = True
            break
    if not is_found:
        raise NotImplementedError
    if "a" <= letter <= "z":
        return ord(letter) - ord("a") + 1
    if "A" <= letter <= "Z":
        return ord(letter) - ord("A") + 27
    raise NotImplementedError


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(line.strip())
    print(result)


if __name__ == "__main__":
    main()
