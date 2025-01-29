FILENAME = "demo2.txt"  # expected 10
FILENAME = "input.txt"


def main() -> None:
    the_list = []
    with open(FILENAME, "r") as file:
        for line in file:
            if line[0] == "+":
                the_list.append(int(line[1:]))
            else:
                the_list.append(int(line))
    result = 0
    visited = {0}
    while True:
        for value in the_list:
            result += value
            if result in visited:
                print(result)
                return
            visited.add(result)


if __name__ == "__main__":
    main()
