FILENAME = "demo.txt"  # expected 20
FILENAME = "input.txt"

ELF = "#"
EMPTY = "."
FOUR = 4


def print_elfes(elfes: dict[tuple[int, int], int]) -> None:
    for y in range(15):
        for x in range(15):
            if (y, x) in elfes:
                print(elfes[y, x] % 10, end=" ")
            else:
                print(EMPTY, end=" ")
        print()


def check(check_index: int, y: int, x: int, elfes: dict[tuple[int, int], int]) -> bool:
    if check_index == 0:
        return (
            (y - 1, x - 1) not in elfes
            and (y - 1, x) not in elfes
            and (y - 1, x + 1) not in elfes
        )
    if check_index == 1:
        return (
            (y + 1, x - 1) not in elfes
            and (y + 1, x) not in elfes
            and (y + 1, x + 1) not in elfes
        )
    if check_index == 2:
        return (
            (y - 1, x - 1) not in elfes
            and (y, x - 1) not in elfes
            and (y + 1, x - 1) not in elfes
        )

    if check_index == 3:
        return (
            (y - 1, x + 1) not in elfes
            and (y, x + 1) not in elfes
            and (y + 1, x + 1) not in elfes
        )
    raise NotImplementedError


def move(check_index: int, y: int, x: int) -> tuple[int, int]:
    if check_index == 0:
        return y - 1, x
    if check_index == 1:
        return y + 1, x
    if check_index == 2:
        return y, x - 1
    if check_index == 3:
        return y, x + 1
    raise NotImplementedError


def main() -> None:
    elfes: dict[tuple[int, int], int] = dict()
    elf_index = 0
    y = 0
    with open(FILENAME, "r") as file:
        for line in file:
            for x, symbol in enumerate(line.strip()):
                if symbol == ELF:
                    elfes[y, x] = elf_index
                    elf_index += 1
            y += 1
    # print(elfes)
    # print_elfes(elfes)
    step = 0
    some_elf_moved = True
    while some_elf_moved:
        some_elf_moved = False
        proposed: dict[tuple[int, int], tuple[int, int] | None] = dict()
        for elf in elfes:
            y, x = elf
            check_all = [check(l, y, x, elfes) for l in range(FOUR)]
            if all(check_all):
                continue
            for check_index in range(step, step + FOUR):
                if check_all[check_index % FOUR]:
                    proposed_move = move(check_index % FOUR, y, x)
                    if proposed_move in proposed:
                        proposed[proposed_move] = None
                    else:
                        proposed[proposed_move] = (y, x)
                    break
        # print(f"step = {step} start_from = {step%FOUR} proposed = {proposed}")
        for target, source in proposed.items():
            if source is None:
                continue
            if target in elfes:
                print(f"target = {target}")
                raise NotImplementedError
            if source not in elfes:
                print(f"source = {source}")
                raise NotImplementedError
            elfes[target] = elfes[source]
            del elfes[source]
            some_elf_moved = True
        # print(f"elfes = {elfes}")
        # print_elfes(elfes)
        step += 1
    print(step)


if __name__ == "__main__":
    main()
