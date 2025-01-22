FILENAME = "demo.txt"  # expected 306
FILENAME = "input.txt"


def main() -> None:
    is_p1_input = True
    p1 = []
    p2 = []
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                if not is_p1_input:
                    raise NotImplementedError
                is_p1_input = False
            elif line.startswith("Player"):
                continue
            elif is_p1_input:
                p1.append(int(line))
            else:
                p2.append(int(line))
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    while len(p1) > 0 and len(p2) > 0:
        a = p1.pop(0)
        b = p2.pop(0)
        if a > b:
            p1.append(a)
            p1.append(b)
        elif a < b:
            p2.append(b)
            p2.append(a)
        else:
            raise NotImplementedError
    if len(p1) == 0 and len(p2) > 0:
        p = p2
    elif len(p2) == 0 and len(p1) > 0:
        p = p1
    else:
        raise NotImplementedError
    result = 0
    for index in range(len(p)):
        result += p[index] * (len(p) - index)
    print(result)


if __name__ == "__main__":
    main()
