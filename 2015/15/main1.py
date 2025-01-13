import re
import itertools

# FILENAME = "demo.txt"  # expected 62842880
FILENAME = "input.txt"
WEIGHT = 100


def f(
    recipe: tuple[str, ...], ingredients: dict[str, tuple[int, int, int, int, int]]
) -> int:
    capacity, durability, flavor, texture = 0, 0, 0, 0
    for ingredient in recipe:
        capacity += ingredients[ingredient][0]
        durability += ingredients[ingredient][1]
        flavor += ingredients[ingredient][2]
        texture += ingredients[ingredient][3]
    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)
    return capacity * durability * flavor * texture


def main() -> None:
    ingredients: dict[str, tuple[int, int, int, int, int]] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            ingredients[line_match.group(1)] = (
                int(line_match.group(2)),
                int(line_match.group(3)),
                int(line_match.group(4)),
                int(line_match.group(5)),
                int(line_match.group(6)),
            )
    print(ingredients)
    best_result = None
    for recipe in itertools.combinations_with_replacement(ingredients.keys(), WEIGHT):
        result = f(recipe, ingredients)
        if best_result is None or best_result < result:
            best_result = result
    print(best_result)


if __name__ == "__main__":
    main()
