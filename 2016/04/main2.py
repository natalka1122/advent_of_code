import re

FILENAME = "demo2.txt"  # expected very encrypted name 343
FILENAME = "input.txt"


def f(line: str) -> None:
    line_match = re.match(r"^([a-z\-]+)(\d+)\[([a-z]+)\]$", line)
    if line_match is None:
        return
    checksum = line_match.group(3)
    if len(checksum) != 5:
        return
    encripted_name = line_match.group(1)
    encripted_name_letters = re.findall(r"[a-z]", encripted_name)
    the_dict = dict()
    for letter in encripted_name_letters:
        if letter not in the_dict:
            the_dict[letter] = 1
        else:
            the_dict[letter] += 1
    if (
        "".join(
            map(lambda x: x[0], sorted(the_dict.items(), key=lambda x: (-x[1], x[0])))
        )[:5]
        != checksum
    ):
        return
    id = int(re.findall(r"(\d+)", line)[0])
    for letter in encripted_name:
        if letter == "-":
            symbol = " "
        else:
            num = (ord(letter) - ord("a") + id) % 26
            symbol = chr(ord("a") + num)
        print(symbol, end="")
    print(int(re.findall(r"(\d+)", line)[0]))


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            f(line.strip())


if __name__ == "__main__":
    main()
