FILENAME, COUNT = "demo.txt", 5  # expected baedc
FILENAME, COUNT = "input.txt", 16

SPIN = "s"
EXCHANGE = "x"
PARTNER = "p"


def main() -> None:
    programs = [chr(x) for x in range(ord("a"), ord("a") + COUNT)]
    with open(FILENAME, "r") as file:
        for line in file:
            for elem in line.split(","):
                if elem[0] == SPIN:
                    size = int(elem[1:])
                    programs = programs[-size:] + programs[:-size]
                elif elem[0] == EXCHANGE:
                    a, b = map(int, elem[1:].split("/"))
                    programs[a], programs[b] = programs[b], programs[a]
                elif elem[0] == PARTNER:
                    a, b = map(lambda x: programs.index(x), elem[1:].split("/"))
                    programs[a], programs[b] = programs[b], programs[a]
    print("".join(programs))


if __name__ == "__main__":
    main()
