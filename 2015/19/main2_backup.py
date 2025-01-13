import re

FILENAME = "demo2_1.txt"  # expected 3
# FILENAME = "demo2_2.txt"  # expected 6
FILENAME = "input.txt"
E = "e"
MY_REGEX = re.compile(r"([A-Z][a-z]*|e)")


def f(lines: set[str], replacements: dict[str, set[str]]) -> set[str]:
    if len(lines) == 0:
        raise NotImplementedError
    result = set()
    for line in lines:
        for index in range(len(line)):
            for source, targets in replacements.items():
                if line[index:].startswith(source):
                    for target in targets:
                        if len(target) < len(source):
                            value = line[:index] + target + line[index + len(source) :]
                            # if len(value) < len(line):
                            result.add(value)
    # print(result)
    return result


def find_all(
    BC: set[tuple[str, ...]],
    T: dict[tuple[int, int], set[tuple[str, ...]]],
    start_pos: int,
    length: int,
) -> bool:
    if length < 0:
        return False
    if length == 0:
        if len(BC) == 0:
            return True
        return False
    if len(BC) == 0:
        return False
    print(f"BC = {BC}")
    if len(BC) == 1:
        raise NotImplementedError
    else:
        raise NotImplementedError
    return False


def main() -> None:
    replacements: dict[str, set[tuple[str, ...]]] = dict()
    final_line = False
    target_line = None
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                if final_line:
                    raise NotImplementedError
                final_line = True
            elif final_line:
                target_line = MY_REGEX.findall(line)
            else:
                a, b = line.split(" => ")
                a_split = tuple(MY_REGEX.findall(a))
                if len(a_split) != 1:
                    raise NotImplementedError
                if a not in replacements:
                    replacements[a] = set()
                b_split = tuple(MY_REGEX.findall(b))
                replacements[a].add(b_split)
    if target_line is None:
        raise NotImplementedError
    print(f"target_line = {target_line}")
    print(replacements)
    T: dict[tuple[int, int], set[tuple[str, ...]]] = dict()
    n = len(target_line)
    for i in range(n):
        if target_line[i] in replacements:
            T[(i, 1)] = set()
            for elem in replacements[target_line[i]]:
                T[(i, 1)].add((target_line[i],))
    print(f"T = {T}")
    raise NotImplementedError
    for j in range(2, n):
        for i in range(n - j):
            print(f"j = {j} i = {i}")
            for A, BC in replacements.items():
                print(f"j = {j} i = {i} A = {A} BC = {BC}")
                if find_all(BC, T, i, j):
                    if (i, j) not in T:
                        T[(i, j)] = set()
                    T[(i, j)].add((A,))
    print(f"T = {T}")

    # step = 0
    # state = {target_line}
    # while True:
    #     if step % 1 == 0:
    #         print(step, len(state))
    #     step += 1
    #     state = f(state, replacements)
    #     if E in state:
    #         break
    # print(step)


if __name__ == "__main__":
    main()
