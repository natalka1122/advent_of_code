from queue import Queue

# FILENAME = "demo.txt"  # expected 7
FILENAME = "input.txt"


def f(start: int, target: int, togglers: list[int]) -> int:
    if start == target:
        return 0
    Q: Queue[tuple[int, int]] = Queue()
    Q.put((start, 0))
    visited: set[int] = set([start])
    while Q.qsize() > 0:
        current, steps = Q.get()
        for t in togglers:
            value = current ^ t
            if value in visited:
                continue
            visited.add(value)
            if value == target:
                return steps + 1
            Q.put((value, steps + 1))
    raise NotImplementedError


def p(togglers_str: str, length: int) -> int:
    togglers = list(map(int, togglers_str[1:-1].split(",")))
    result = ["0"] * length
    for t in togglers:
        if result[int(t)] == "1":
            raise NotImplementedError
        result[t] = "1"
    return int("".join(result), 2)


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(" ")
            target_length = len(line[0]) - 2
            target = int("".join((map(lambda x: "1" if x == "#" else "0", line[0][1:-1]))), 2)
            togglers = list(map(lambda x: p(x, target_length), line[1:-1]))
            result += f(0, target, togglers)
    print(result)


if __name__ == "__main__":
    main()
