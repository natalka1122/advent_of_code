FILENAME = "demo.txt"  # expect 70
# FILENAME = "input.txt"


def f(line: list[str]) -> int:
    if len(line) != 3:
        raise NotImplementedError
    is_found = False
    for letter in line[0]:
        if letter in line[1] and letter in line[2]:
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
    elfes = []
    with open(FILENAME, "r") as file:
        for line in file:
            elfes.append(line.strip())
            if len(elfes) == 3:
                result += f(elfes)
                elfes = []
    print(result)


if __name__ == "__main__":
    main()
