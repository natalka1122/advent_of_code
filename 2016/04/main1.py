import re

FILENAME = "demo1.txt"  # expected 1514
FILENAME = "input.txt"


def check(line: str) -> bool:
    line_match = re.match(r"^([a-z\-]+)(\d+)\[([a-z]+)\]$", line)
    if line_match is None:
        return False
    checksum = line_match.group(3)
    if len(checksum) != 5:
        return False
    encripted_name = line_match.group(1)
    encripted_name_letters = re.findall(r"[a-z]", encripted_name)
    the_dict = dict()
    for letter in encripted_name_letters:
        if letter not in the_dict:
            the_dict[letter] = 1
        else:
            the_dict[letter] += 1
    return (
        "".join(
            map(lambda x: x[0], sorted(the_dict.items(), key=lambda x: (-x[1], x[0])))
        )[:5]
        == checksum
    )


def f(line: str) -> int:
    if not check(line):
        return 0
    return int(re.findall(r"(\d+)", line)[0])


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(line.strip())
    print(result)


if __name__ == "__main__":
    main()
