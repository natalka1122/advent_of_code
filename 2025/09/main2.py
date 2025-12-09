# FILENAME = "demo.txt"  # expected 24
FILENAME = "input.txt"


def main() -> None:
    reds: list[tuple[int, int]] = []
    y_set: set[int] = set()
    x_set: set[int] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            y, x = map(int, line.strip().split(","))
            y_set.add(y)
            y_set.add(y + 1)
            y_set.add(y - 1)
            x_set.add(x)
            x_set.add(x - 1)
            x_set.add(x + 1)
            reds.append((y, x))
    y_list = sorted(y_set)
    x_list = sorted(x_set)
    border: set[tuple[int, int]] = set()
    for i in range(-1, len(reds) - 1):
        y0 = min(reds[i][0], reds[i + 1][0])
        y1 = max(reds[i][0], reds[i + 1][0])
        x0 = min(reds[i][1], reds[i + 1][1])
        x1 = max(reds[i][1], reds[i + 1][1])
        for y_ in y_list[y_list.index(y0) : y_list.index(y1) + 1]:
            for x_ in x_list[x_list.index(x0) : x_list.index(x1) + 1]:
                border.add((y_, x_))

    outside_set: set[tuple[int, int]] = set([(y_list[0], x_list[0])])
    Q: set[tuple[int, int]] = set([(y_list[0], x_list[0])])
    while len(Q) > 0:
        current = Q.pop()
        if current not in outside_set:
            raise NotImplementedError
        y_index0 = y_list.index(current[0])
        x_index0 = x_list.index(current[1])
        for y_index in range(max(0, y_index0 - 1), min(y_index0 + 2, len(y_list))):
            for x_index in range(max(0, x_index0 - 1), min(x_index0 + 2, len(x_list))):
                coord = y_list[y_index], x_list[x_index]
                if coord in outside_set or coord in border:
                    continue
                Q.add(coord)
                outside_set.add(coord)

    best = 0
    for i in range(len(reds)):
        for j in range(i):
            y0 = min(reds[i][0], reds[j][0])
            y1 = max(reds[i][0], reds[j][0])
            x0 = min(reds[i][1], reds[j][1])
            x1 = max(reds[i][1], reds[j][1])
            area = (y1 - y0 + 1) * (x1 - x0 + 1)
            if area > best:
                is_good = True
                for outside in outside_set:
                    if y0 < outside[0] < y1 and x0 < outside[1] < x1:
                        is_good = False
                        break
                if is_good:
                    best = area
    print(best)


if __name__ == "__main__":
    main()
