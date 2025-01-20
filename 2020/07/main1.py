import re

FILENAME = "demo.txt"  # expected 4
FILENAME = "input.txt"

TARGET = "shiny gold"


def main() -> None:
    bags: dict[str, set[str]] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"([a-z]+ [a-z]+) bags contain ((no other bags)|([\d\w ,]+))\.",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            # print(line_match.groups())
            name = line_match.group(1)
            if name in bags:
                raise NotImplementedError
            bags[name] = set()
            if line_match.group(4) is not None:
                current_bags = re.findall(r"\d+ ([a-z]+ [a-z]+) bags?", line_match.group(4))
                # print(current_bags)
                bags[name].update(current_bags)
    is_changed = True
    while is_changed:
        is_changed = False
        for bag_name1 in bags:
            for bag_name2 in bags[bag_name1]:
                if bag_name2 not in bags:
                    continue
                current_size = len(bags[bag_name1])
                bags[bag_name1].update(bags[bag_name2])
                if len(bags[bag_name1]) != current_size:
                    is_changed = True
                    break
            if is_changed:
                break
    # print(bags)
    result = 0
    for bag_set in bags.values():
        if TARGET in bag_set:
            result += 1
    print(result)


if __name__ == "__main__":
    main()
