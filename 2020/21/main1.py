import re

FILENAME = "demo.txt"  # expected 5
FILENAME = "input.txt"


def main() -> None:
    allergens: dict[str, set[int]] = dict()
    solution: dict[str, set[str]] = dict()
    labels: list[tuple[set[str], set[str]]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"([\w ]+) \(contains ([\w ,]+)\)", line.strip())
            if line_match is None:
                raise NotImplementedError
            current_foods = set(line_match.group(1).split(" "))
            current_allergens = set(line_match.group(2).split(", "))
            for allergen in current_allergens:
                if allergen not in allergens:
                    allergens[allergen] = set()
                allergens[allergen].add(len(labels))
            labels.append((current_foods, current_allergens))
    # print(f"labels = {labels}")
    # print(f"allergens = {allergens}")
    for allergen in allergens:
        intersect = None
        for index in allergens[allergen]:
            if intersect is None:
                intersect = labels[index][0]
            else:
                intersect = intersect.intersection(labels[index][0])
        if intersect is None:
            raise NotImplementedError
        print(f"found {allergen} = {intersect}")
        solution[allergen] = intersect
    is_changed = True
    while is_changed:
        is_changed = False
        for allergen0 in allergens:
            if len(solution[allergen0]) == 1:
                for food0 in solution[allergen0]:
                    for allergen1 in allergens:
                        if allergen1 == allergen0:
                            continue
                        if food0 in solution[allergen1]:
                            is_changed = True
                            solution[allergen1].remove(food0)
                            break
                if is_changed:
                    break
    if not all(map(lambda x: len(x), solution.values())):
        raise NotImplementedError
    print(solution)
    bad_ingridients = list(set().union(*solution.values()))
    result = 0
    for label in labels:
        for ingredient in label[0]:
            if ingredient not in bad_ingridients:
                result += 1
    print(result)


if __name__ == "__main__":
    main()
