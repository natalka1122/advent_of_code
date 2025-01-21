FILENAME = "demo.txt"  # expected 295
FILENAME = "input.txt"


def main() -> None:
    timestamp = None
    buses:list[int] = []
    with open(FILENAME, "r") as file:
        for line in file:
            if timestamp is None:
                timestamp = int(line)
            else:
                buses = list(map(int, filter(lambda x: x.isdigit(), line.strip().split(","))))
    if timestamp is None:
        raise NotImplementedError
    print(buses)
    t = 0
    is_found = False
    while not is_found:
        for bus in buses:
            if (timestamp + t) % bus == 0:
                is_found = True
                break
        t += 1
    print(bus * (t - 1))


if __name__ == "__main__":
    main()
