FILENAME = "demo2.txt"  # expected fgij
FILENAME = "input.txt"


def main() -> None:
    lines = []
    with open(FILENAME, "r") as file:
        for line in file:
            lines.append(line.strip())
    for i in range(len(lines[0])):
        for j in range(len(lines)):
            lj = lines[j][:i] + lines[j][i + 1 :]
            for k in range(j + 1, len(lines)):
                if lj == lines[k][:i] + lines[k][i + 1 :]:
                    print(lj)
                    break


if __name__ == "__main__":
    main()
