import functools

FILENAME = "demo2.txt"  # expected ?
FILENAME = "demo.txt"  # expected 291
FILENAME = "input.txt"


@functools.cache
def play(p1: tuple[int, ...], p2: tuple[int, ...]) -> tuple[bool, tuple[int, ...]]:
    visited: set[tuple[int, ...]] = set()
    # print(f"play {p1} vs {p2}")
    while len(p1) > 0 and len(p2) > 0:
        if len(p1) - 1 >= p1[0] and len(p2) - 1 >= p2[0]:
            # print("Call new game")
            p1_win, _ = play(p1[1 : 1 + p1[0]], p2[1 : 1 + p2[0]])
        elif p1[0] > p2[0]:
            p1_win = True
        elif p1[0] < p2[0]:
            p1_win = False
        else:
            raise NotImplementedError
        if p1_win:
            p1 = p1[1:] + (p1[0], p2[0])
            p2 = p2[1:]
        else:
            p2 = p2[1:] + (p2[0], p1[0])
            p1 = p1[1:]

        if p1 in visited:
            # print(f"p1 wins on repeat")
            return True, p1
        visited.add(p1)
        # print(f"p1 = {p1}")
        # print(f"p2 = {p2}")
        if len(visited) % 1000 == 0:
            print(len(visited))

    if len(p1) == 0 and len(p2) > 0:
        # print("p2 wins")
        return False, p2
    elif len(p2) == 0 and len(p1) > 0:
        # print("p1 wins")
        return True, p1
    else:
        raise NotImplementedError


def main() -> None:
    is_p1_input = True
    p1: tuple[int, ...] = tuple()
    p2: tuple[int, ...] = tuple()
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                if not is_p1_input:
                    raise NotImplementedError
                is_p1_input = False
            elif line.startswith("Player"):
                continue
            elif is_p1_input:
                p1 = p1 + (int(line),)
            else:
                p2 = p2 + (int(line),)
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    _, p_win = play(p1, p2)
    result = 0
    for index in range(len(p_win)):
        result += p_win[index] * (len(p_win) - index)
    print(result)


if __name__ == "__main__":
    main()
