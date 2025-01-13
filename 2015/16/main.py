FILENAME = "input.txt"
EQ = "eq"
LT = "lt"
GT = "gt"
TARGET_SUE = {
    "children": (3, EQ),
    "cats": (7, GT),
    "samoyeds": (2, EQ),
    "pomeranians": (3, LT),
    "akitas": (0, EQ),
    "vizslas": (0, EQ),
    "goldfish": (5, LT),
    "trees": (3, GT),
    "cars": (2, EQ),
    "perfumes": (1, EQ),
}


def main() -> None:
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(": ", 1)
            index = int(line[0].split(" ")[1])
            found = True
            for pair in line[1].split(", "):
                a = pair.split(": ")[0]
                b = int(pair.split(": ")[1])
                if a not in TARGET_SUE:
                    raise NotImplementedError
                if TARGET_SUE[a][1] == EQ:
                    if TARGET_SUE[a][0] != b:
                        found = False
                elif TARGET_SUE[a][1] == LT:
                    if TARGET_SUE[a][0] <= b:
                        found = False
                elif TARGET_SUE[a][1] == GT:
                    if TARGET_SUE[a][0] >= b:
                        found = False
                else:
                    raise NotImplementedError
            if found:
                print(index)
                break


if __name__ == "__main__":
    main()
