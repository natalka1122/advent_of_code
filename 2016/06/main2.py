FILENAME = "demo.txt"  # expected advent
FILENAME = "input.txt"


def main() -> None:
    result: list[dict[str, int]] = []
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            for index, symbol in enumerate(line):
                if len(result) == index:
                    result.append({symbol: 1})
                elif symbol not in result[index]:
                    result[index][symbol] = 1
                else:
                    result[index][symbol] += 1
    for index in range(len(result)):
        print(sorted(result[index].items(), key=lambda x: (x[1]))[0][0], end="")
    print()


if __name__ == "__main__":
    main()
