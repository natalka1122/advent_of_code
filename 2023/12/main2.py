from __future__ import annotations
import functools

# FILENAME = "demo.txt"
# FILENAME = "demo1.txt"
FILENAME = "input.txt"

@functools.cache
def find_combinations_v2(
    amount: int, total: int, springs: str, cgroups: tuple[int, ...]
) -> int:
    if amount == 1 and total == 0:
        return 1
    if amount == 0 or total < 0:
        return 0
    if len(cgroups) == 0:
        for symbol in springs:
            if symbol == "#":
                return 0
        return 1
    result = 0
    for i in range(total + 1):
        is_good = True
        # new_line = ""
        for j in range(i):
            # new_line += "."
            if springs[j] == "#":
                is_good = False
                break
        if not is_good:
            continue
        for j in range(i, i + cgroups[0]):
            # new_line += "#"
            if springs[j] == ".":
                is_good = False
                break
        if not is_good:
            continue
        # new_line +="."
        if springs[i + cgroups[0]] == "#":
            is_good = False
        if not is_good:
            continue
        result += find_combinations_v2(
            amount=amount - 1,
            total=total - i,
            springs=springs[i + cgroups[0] + 1 :],
            cgroups=cgroups[1:],
        )
    return result


def f(springs: str, cgroups: tuple[int, ...]) -> int:
    blocks = len(cgroups) + 1
    block_sum = len(springs) + 1 - sum(cgroups) - len(cgroups)
    return find_combinations_v2(blocks, block_sum, springs + ".", cgroups)


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(" ")
            springs = line[0]
            cgroups = list(map(int, line[1].split(",")))
            r = f(((springs + "?") * 5)[:-1], tuple(cgroups * 5))
            print(f"line = {line} r = {r}")
            result += r
    print(result)


if __name__ == "__main__":
    main()
