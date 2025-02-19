from __future__ import annotations

# FILENAME = "demo.txt"
# FILENAME = "demo2.txt"
FILENAME = "input.txt"


def f(update, pages):
    print(f"update = {update}")
    for i in range(len(update) - 1):
        if update[i] not in pages:
            continue
        for j in range(i, len(update)):
            if update[j] in pages[update[i]]:
                return 0
    print(update[len(update) // 2])
    return update[len(update) // 2]


def main():
    result = 0
    with open(FILENAME, "r") as file:
        pages: dict[int, set[int]] = dict()
        # updates: list[int] = []
        read_pages = True
        for line_ in file:
            line = line_.strip()
            if not line:
                if read_pages == False:
                    raise NotImplementedError
                read_pages = False
                print(pages)
            elif read_pages:
                b, a = map(int, line.split("|"))
                if a in pages:
                    pages[a].add(b)
                else:
                    pages[a] = {b}
            else:
                # updates.append(list(map(int,line.split(","))))
                update = list(map(int, line.split(",")))
                result += f(update, pages)
    # print(updates)
    print(result)


if __name__ == "__main__":
    main()
