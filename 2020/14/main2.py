from collections.abc import Iterator
import re

FILENAME = "demo2.txt"  # expected 208
FILENAME = "input.txt"

X = "X"

def g(line:str) -> Iterator[int]:
    if X not in line:
        yield int(line,base=2)
        return
    x_index = line.index(X)
    for v in [0,1]:
        yield from g(line[:x_index]+str(v)+line[x_index+1:])
    


def f(num: int, mask: str) -> Iterator[int]:
    num_binary = bin(num)[2:]
    num_binary = "0" * (len(mask) - len(num_binary)) + num_binary
    value = ""
    for index in range(len(mask)):
        if mask[index] == "0":
            value += num_binary[index]
        else:
            value += mask[index]
    yield from g(value)
            


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
                for current_index in f(index, mask):
                    result[current_index] = num

    # print(result)
    print(sum(result.values()))


if __name__ == "__main__":
    main()
