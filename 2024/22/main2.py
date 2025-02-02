from __future__ import annotations

# FILENAME, STEPS = "demo2.txt", 2000  # expected 23
# FILENAME, STEPS = "demo123.txt", 10  # expected ?
FILENAME, STEPS = "input.txt", 2000
FOUR = 4


def prune(n: int) -> int:
    return n % 16777216


def mix(a: int, b: int) -> int:
    return a ^ b


def calc(n: int) -> int:
    n = prune(mix(n * 64, n))
    n = prune(mix(n // 32, n))
    n = prune(mix(n * 2048, n))
    return n


def f(n: int) -> list[int]:
    result = [n]
    for _ in range(STEPS - 1):
        n = calc(n)
        result.append(n)
    return result


def transform(l: list[int]) -> list[int]:
    result = []
    for i in range(len(l) - 1):
        result.append(l[i + 1] % 10 - l[i] % 10)
    return result


def main():
    the_dict: dict[tuple[int, int, int, int], int] = dict()
    step = 0
    with open(FILENAME, "r") as file:
        for line in file:
            print(step)
            step += 1
            f_line = f(int(line.strip()))
            transform_line = transform(f_line)
            for i in range(len(transform_line) - FOUR):
                current = tuple(transform_line[i : i + FOUR])
                if current in the_dict:
                    if step not in the_dict[current]:
                        the_dict[current][step] = f_line[i + FOUR] % 10
                else:
                    the_dict[current] = {step: f_line[i + FOUR] % 10}
    result_dict = dict()
    for key in the_dict:
        result_dict[key] = sum(the_dict[key].values())
    print(max(result_dict.values()))


if __name__ == "__main__":
    main()
