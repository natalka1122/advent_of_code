from __future__ import annotations
from typing import Iterator

# FILENAME = "demo.txt"
# FILENAME = "demo1.txt"
FILENAME = "input.txt"


def find_combinations(
    amount: int, total: int, current: list[int] = []
) -> Iterator[list[int]]:
    if amount == 0 and total == 0:
        yield current
        return
    elif amount == 0 or total < 0:
        return

    for i in range(total + 1):
        yield from find_combinations(amount - 1, total - i, current + [i])


def find_combinations_v2(
    amount: int, total: int, springs: str, cgroups: list[int]
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


def f(springs: str, cgroups: list[int]) -> int:
    # print(f"springs = {springs} cgroups = {cgroups}")
    blocks = len(cgroups) + 1
    block_sum = len(springs) + 1 - sum(cgroups) - len(cgroups)
    # print(f"broken = {broken} working = {working} blocks = {blocks} block_sum = {block_sum}")
    # print(f"blocks = {blocks} block_sum = {block_sum}")
    return find_combinations_v2(blocks, block_sum, springs + ".", cgroups)
    result = 0
    for combination in find_combinations(blocks, block_sum):
        line = ""
        for i in range(len(cgroups)):
            line += "." * combination[i] + "#" * cgroups[i] + "."
        line += "." * combination[-1]
        line = line[:-1]
        # print(springs)
        # print(line)
        # raise NotImplementedError
        bad_line = False
        for i in range(len(line)):
            if springs[i] == "." and line[i] != ".":
                bad_line = True
                break
            if springs[i] == "#" and line[i] != "#":
                bad_line = True
                break
        if not bad_line:
            result += 1
        # else:
        #     print(line)
    return result


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(" ")
            springs = line[0]
            cgroups = list(map(int, line[1].split(",")))
            r = f(((springs + "?") * 5)[:-1], cgroups * 5)
            # r = f(springs, cgroups)
            print(f"line = {line} r = {r}")
            result += r
            # result += f(springs, cgroups)
    print(result)


if __name__ == "__main__":
    main()
