from __future__ import annotations

# FILENAME = "demo1.txt"  # expected 37327623
# FILENAME = "demo123.txt"  # expected ?
FILENAME = "input.txt"
STEPS = 2000


def prune(n: int) -> int:
    return n % 16777216


def mix(a: int, b: int) -> int:
    return a ^ b


def calc(n: int) -> int:
    n = prune(mix(n * 64, n))
    n = prune(mix(n // 32, n))
    n = prune(mix(n * 2048, n))
    return n


def f(n: int) -> int:
    for _ in range(STEPS):
        n = calc(n)
    print(n)
    return n


def main():
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(int(line.strip()))
    print(result)


if __name__ == "__main__":
    main()
