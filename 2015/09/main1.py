import re
import itertools

FILENAME = "demo.txt"  # expected 605
FILENAME = "input.txt"


def main() -> None:
    cities: dict[str, dict[str, int]] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"(\w+) to (\w+) = (\d+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            city1 = line_match.group(1)
            city2 = line_match.group(2)
            dist = int(line_match.group(3))
            if city1 not in cities:
                cities[city1] = dict()
            cities[city1][city2] = dist
            if city2 not in cities:
                cities[city2] = dict()
            cities[city2][city1] = dist
    best_distance = None
    for path in itertools.permutations(cities.keys()):
        distance = 0
        for i in range(len(path) - 1):
            distance += cities[path[i]][path[i + 1]]
        if best_distance is None:
            best_distance = distance
        else:
            best_distance = min(best_distance, distance)
    print(best_distance)


if __name__ == "__main__":
    main()
