import re

FILENAME = "demo1.txt"  # expected 165
FILENAME = "input.txt"

X = "X"


def f(num: int, mask: str) -> int:
    num_binary = bin(num)[2:]
    num_binary = "0" * (len(mask) - len(num_binary)) + num_binary
    print(num_binary, len(num_binary))
    result = ""
    for index in range(len(mask)):
        if mask[index] == X:
            result += num_binary[index]
        else:
            result += mask[index]
    return int(result, base=2)


def main() -> None:
    result: dict[int, int] = dict()
    mask = None
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if line.startswith("mask = "):
                mask = line.split(" ")[2]
            else:
                if mask is None:
                    raise NotImplementedError
                line_match = re.match(r"mem\[(\d+)\] = (\d+)", line)
                if line_match is None:
                    raise NotImplementedError
                index, num = map(int, line_match.groups())
                result[index] = f(num, mask)

    print(result)
    print(sum(result.values()))


if __name__ == "__main__":
    main()
