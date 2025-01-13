from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"


def find_combinations(amount, total, current=[]):
    if amount == 0 and total == 0:
        yield current
        return
    elif amount == 0 or total < 0:
        return

    for i in range(total + 1):
        yield from find_combinations(amount - 1, total - i, current + [i])


def f(springs, cgroups):
    # print(f"springs = {springs} cgroups = {cgroups}")
    blocks = len(cgroups) + 1
    block_sum = len(springs) + 1 - sum(map(lambda x: x + 1, cgroups))
    # print(f"broken = {broken} working = {working} blocks = {blocks} block_sum = {block_sum}")
    # print(f"blocks = {blocks} block_sum = {block_sum}")
    result = 0
    for combination in find_combinations(blocks, block_sum):
        line = ""
        for i in range(len(cgroups)):
            line += "." * combination[i] + "#" * cgroups[i]+"."
        line += "." * combination[-1]
        line = line[:-1]
        # print(springs)
        # print(line)
        # raise NotImplementedError
        bad_line = False
        for i in range(len(line)):
            if springs[i] =="." and line[i] != ".":
                bad_line = True
                break
            if springs[i] =="#" and line[i]!= "#":
                bad_line = True
                break
        if not bad_line:
            result += 1
        # else:
        #     print(line)
    return result


def main():
    result = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(" ")
            springs = line[0]
            cgroups = list(map(int, line[1].split(",")))
            r =  f(springs, cgroups)
            print(f"line = {line} r = {r}")
            result += r
            # result += f(springs, cgroups)
    print(result)


if __name__ == "__main__":
    main()
