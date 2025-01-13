FILENAME = "input.txt"
TARGET_SUE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
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
                if TARGET_SUE[a] != b:
                    found = False
            if found:
                print(index)
                break


if __name__ == "__main__":
    main()
