from __future__ import annotations

FILENAME = "demo.txt"  # expected 3
FILENAME = "input.txt"
FIVE = 5
EMPTY = "."
FILLED = "#"


def process(current: list[str], locks: set[tuple[int]], keys: set[tuple[int]]) -> None:
    print(current)
    if len(current) != FIVE + 2:
        raise NotImplementedError
    is_lock = all(map(lambda x: x == FILLED, current[0])) and all(
        map(lambda x: x == EMPTY, current[-1])
    )
    is_key = all(map(lambda x: x == EMPTY, current[0])) and all(
        map(lambda x: x == FILLED, current[-1])
    )
    result = []
    for x in range(FIVE):
        result.append(0)
        for y in range(1, FIVE + 1):
            if current[y][x] == FILLED:
                result[-1] += 1
    if is_lock and not is_key:
        print(f"lock = {result}")
        locks.add(tuple(result))
    elif is_key and not is_lock:
        print(f"key = {result}")
        keys.add(tuple(result))
    else:
        raise NotImplementedError


def main():
    keys = set()
    locks = set()
    current = []
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                process(current, locks, keys)
                current = []
            else:
                current.append(line)
    process(current, locks, keys)
    print(f"keys = {keys}")
    print(f"locks = {locks}")
    result = 0
    for key in keys:
        for lock in locks:
            if all(map(lambda x: key[x] + lock[x] <= FIVE, range(FIVE))):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
