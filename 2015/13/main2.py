import re
import itertools

FILENAME = "input.txt"
MYSELF = "myself"


def main() -> None:
    people: dict[str, dict[str, int]] = {MYSELF: dict()}
    with open(FILENAME, "r") as file:
        for line in file:
            gain_match = re.match(
                r"(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)\.",
                line.strip(),
            )
            if gain_match is None:
                raise NotImplementedError
            name1 = gain_match.group(1)
            name2 = gain_match.group(4)
            if gain_match.group(2) == "gain":
                diff = int(gain_match.group(3))
            elif gain_match.group(2) == "lose":
                diff = -int(gain_match.group(3))
            else:
                raise NotImplementedError
            if name1 not in people:
                people[name1] = {MYSELF: 0}
                people[MYSELF][name1] = 0
            people[name1][name2] = diff
    print(people)
    best_result = None
    for path_ in itertools.permutations(filter(lambda x: x != MYSELF, people.keys())):
        path = path_ + (MYSELF,)
        result = 0
        for index in range(len(path)):
            index_plus_1 = index + 1
            if index_plus_1 == len(path):
                index_plus_1 = 0
            index_minus_1 = index - 1
            if index_minus_1 == -1:
                index_minus_1 = len(path) - 1
            result += (
                people[path[index]][path[index_plus_1]]
                + people[path[index]][path[index_minus_1]]
            )
        print(path, result)
        if best_result is None or result > best_result:
            best_result = result
    print(best_result)


if __name__ == "__main__":
    main()
