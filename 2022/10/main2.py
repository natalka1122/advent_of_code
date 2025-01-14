FILENAME = "demo2.txt"
FILENAME = "input.txt"


def main() -> None:
    step = 0
    sprite = 0
    current = ""
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if line == "noop":
                step += 1
                if sprite <= len(current) < sprite + 3:
                    current += "#"
                else:
                    current += "."
            elif line.startswith("addx "):
                step += 1
                if sprite <= len(current) < sprite + 3:
                    current += "#"
                else:
                    current += "."
                step += 1
                if sprite <= len(current) < sprite + 3:
                    current += "#"
                else:
                    current += "."
                sprite += int(line.split(" ")[1])
            else:
                raise NotImplementedError
            if len(current) >= 40:
                print(current[:40])
                current = current[40:]


if __name__ == "__main__":
    main()
