import re

FILENAME = "demo.txt"  # expected 32
FILENAME = "demo2.txt"  # expected 126
FILENAME = "input.txt"

TARGET = "shiny gold"


def f(bag_name: str, bags: dict[str, list[tuple[int, str]]]) -> int:
    if bag_name not in bags:
        return 0
    if len(bags[bag_name]) == 0:
        return 0
    result = 0
    for bag_count, name in bags[bag_name]:
        result += bag_count * (1 + f(name, bags))
    return result


def main() -> None:
    bags: dict[str, list[tuple[int, str]]] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"([a-z]+ [a-z]+) bags contain ((no other bags)|([\d\w ,]+))\.",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            name = line_match.group(1)
            if name in bags:
                raise NotImplementedError
            bags[name] = []
            if line_match.group(4) is not None:
                current_bags = re.findall(r"(\d+) ([a-z]+ [a-z]+) bags?", line_match.group(4))
                bags[name].extend(map(lambda x: (int(x[0]), x[1]), current_bags))
                # print(bags[name])

    print(f(TARGET, bags))


if __name__ == "__main__":
    main()
