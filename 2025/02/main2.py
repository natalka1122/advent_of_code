import re

# FILENAME = "demo.txt"
FILENAME = "input.txt"


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        line = file.readline()
        for pair in line.split(","):
            elems = list(map(int, pair.split("-")))
            for elem in range(elems[0], elems[1] + 1):
                elem_str = str(elem)
                if re.match(r"(\d+)(\1+)$", elem_str):
                    result += elem
    print(result)


if __name__ == "__main__":
    main()
