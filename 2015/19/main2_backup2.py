from typing import Iterator
import re

FILENAME = "demo2_1.txt"  # expected 3
# FILENAME = "demo2_2.txt"  # expected 6
# FILENAME = "input.txt"
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
                            result.add(value)
    return result


def generate_name() -> Iterator[str]:
    i = 1
    while True:
        result = str(i)
        result = "0" * (3 - len(result)) + result
        yield result
        i += 1


def main() -> None:
    replacements: dict[str, set[tuple[str] | tuple[str, str]]] = dict()
    final_line = False
    target_line = None
    generated_name = generate_name()
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
                b_split = tuple(MY_REGEX.findall(b))
                if len(b_split) == 0:
                    raise NotImplementedError
                if len(b_split) == 1:
                    if a not in replacements:
                        replacements[a] = set()
                    replacements[a].add(b_split)
                else:
                    names = [a]
                    targets = []
                    for i in range(len(b_split) - 2):
                        name = next(generated_name)
                        names.append(name)
                        targets.append(b_split[i])
                        targets.append(name)
                    targets.append(b_split[-2])
                    targets.append(b_split[-1])
                    for i in range(len(names)):
                        if names[i] not in replacements:
                            replacements[names[i]] = set()
                        replacements[names[i]].add((targets[2 * i], targets[2 * i + 1]))
    if target_line is None:
        raise NotImplementedError
    print(f"target_line = {target_line}")
    print(f"replacements = {replacements}")
    T: dict[tuple[int, int], set[str]] = dict()
    n = len(target_line)
    for i in range(n):
        for key, value in replacements.items():
            for item in value:
                length = len(item)
                if tuple(target_line[i : i + length]) == item:
                    if (i, length) not in T:
                        T[i, length] = set()
                    T[i, length].add(key)
    print(f"T = {T}")

    for j in range(2, n + 1):
        for i in range(n - j + 1):
            for k in range(1, j):
                for A, set_BC in replacements.items():
                    for BC in set_BC:
                        if len(BC) == 1:
                            continue
                        B, C = BC
                        if B in T[i, k] and C in T[i + k, j - k]:
                            print(
                                f"j = {j} i = {i} k = {k} A = {A} B = {B} C = {C} BC = {BC}"
                            )
                            if (i, j) not in T:
                                T[(i, j)] = set()
                            T[(i, j)].add(A)
    print(f"T = {T}")


if __name__ == "__main__":
    main()
