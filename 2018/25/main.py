FILENAME = "demo2.txt"  # expected 2
FILENAME = "demo4.txt"  # expected 4
FILENAME = "demo3.txt"  # expected 3
FILENAME = "demo8.txt"  # expected 8
FILENAME = "input.txt"

MAX_DISTANCE = 3
Quadriple = tuple[int, int, int, int]


def dist(p1: Quadriple, p2: Quadriple) -> int:
    return sum(map(lambda x: abs(p1[x] - p2[x]), range(4)))


def main() -> None:
    stars: set[Quadriple] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            parsed_line = tuple(map(int, line.strip().split(",")))
            if len(parsed_line) != 4:
                raise NotImplementedError
            stars.add(parsed_line)
    result = 0
    while len(stars) > 0:
        result += 1
        constellation = [stars.pop()]
        while len(constellation) > 0:
            current = constellation.pop()
            add_stars = []
            for star in stars:
                if dist(current, star) <= 3:
                    add_stars.append(star)
            for star in add_stars:
                constellation.append(star)
                stars.remove(star)
    print(result)


if __name__ == "__main__":
    main()
