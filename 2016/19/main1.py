FILENAME = "demo.txt"  # expected 3
FILENAME = "input.txt"


def f(n: int) -> int:
    elfes = set(range(1, n + 1))
    pointer = 0
    while len(elfes) > 1:
        for elf in sorted(elfes):
            if pointer == 1:
                elfes.remove(elf)
                if len(elfes) % 10000 ==0:
                    print(f"left {len(elfes)}")
            pointer = 1 - pointer

    return elfes.pop()


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(int(line)))


if __name__ == "__main__":
    main()
