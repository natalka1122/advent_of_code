FILENAME, COUNT = "demo.txt", 5
FILENAME, COUNT = "input.txt", 16

SPIN = "s"
EXCHANGE = "x"
PARTNER = "p"
BILLION = 1000000000


def main() -> None:
    programs = [chr(x) for x in range(ord("a"), ord("a") + COUNT)]
    with open(FILENAME, "r") as file:
        for line in file:
            operations = line.split(",")
    p_dict: dict[str, int] = dict()
    index = 0
    while index < BILLION:
        p_value = "".join(programs)
        if p_value in p_dict:
            print(index, p_dict[p_value], BILLION % index)
            if p_dict[p_value] == 0:
                break
            else:
                raise NotImplementedError
        p_dict[p_value] = index
        for elem in operations:
            if elem[0] == SPIN:
                size = int(elem[1:])
                programs = programs[-size:] + programs[:-size]
            elif elem[0] == EXCHANGE:
                a, b = map(int, elem[1:].split("/"))
                programs[a], programs[b] = programs[b], programs[a]
            elif elem[0] == PARTNER:
                a, b = map(lambda x: programs.index(x), elem[1:].split("/"))
                programs[a], programs[b] = programs[b], programs[a]
        index += 1
    for key, value in p_dict.items():
        if value == BILLION % index:
            print(key)


if __name__ == "__main__":
    main()
