FILENAME, LEN_PREAMBLE = "demo.txt", 5  # expected 127
FILENAME, LEN_PREAMBLE = "input.txt", 25


def main() -> None:
    preamble: list[int] = []
    with open(FILENAME, "r") as file:
        for line in file:
            if len(preamble) < LEN_PREAMBLE:
                preamble.append(int(line))
            else:
                current = int(line)
                found_flag = False
                for i in range(1, LEN_PREAMBLE):
                    for j in range(i):
                        if preamble[i] + preamble[j] == current:
                            found_flag = True
                            break
                    if found_flag:
                        break
                if not found_flag:
                    print(current)
                    break
                preamble = preamble[1:] + [current]


if __name__ == "__main__":
    main()
