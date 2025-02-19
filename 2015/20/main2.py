# FILENAME = "demo.txt"
FILENAME = "input.txt"
ELEVEN = 11
FIFTY = 50


def f(n: int) -> int:
    the_list = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, min(50 * (i + 1), n + 1), i):
            the_list[j] += i
    for i in range(len(the_list)):
        if the_list[i] >= n:
            return i
    raise NotImplementedError


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(int(line) // ELEVEN))


if __name__ == "__main__":
    main()
