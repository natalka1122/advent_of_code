# from __future__ import annotations
from typing import cast
import re

# FILENAME = "demo.txt"
FILENAME = "input.txt"

START_WORKFLOW = "in"
ACCEPT = "A"
REJECT = "R"
LT = "<"
GT = ">"
MIN_VALUE = 1
MAX_VALUE = 4000 + 1
COORDS = "xmas"
Rule = str | tuple[str, str, int, str]


def square(ul: tuple[int, int, int, int], dr: tuple[int, int, int, int]) -> int:
    result = 1
    for i in range(4):
        if ul[i] >= dr[i]:
            raise NotImplementedError
        result *= dr[i] - ul[i]
    return result


def calc(
    ul: tuple[int, int, int, int],
    dr: tuple[int, int, int, int],
    rules: list[Rule],
    workflows: dict[str, list[Rule]],
):
    if len(rules) == 0:
        raise NotImplementedError
    rule = rules[0]
    print("*" * 20)
    print(f"ul = {ul} dr = {dr} rule = {rule} rules = {rules}")
    result = 0
    if isinstance(rule, str):
        if rule == ACCEPT:
            result += square(ul, dr)
        elif rule == REJECT:
            pass
        else:
            result += calc(ul, dr, workflows[rule], workflows)
    elif isinstance(rule, tuple):
        if rule[0] not in COORDS:
            raise NotImplementedError
        coord_index = COORDS.index(rule[0])
        if rule[1] == LT:
            if rule[2] <= ul[coord_index]:
                raise NotImplementedError
            elif ul[coord_index] < rule[2] < dr[coord_index]:
                ul1 = ul
                dr1_list = list(dr)
                dr1_list[coord_index] = rule[2]
                dr1 = cast(tuple[int, int, int, int], dr1_list)
                print(f"for [{ul[coord_index]},{rule[2]}) [{ul1,dr1}) do {rule[3]}")
                if rule[3] == ACCEPT:
                    result += square(ul1, dr1)
                elif rule[3] == REJECT:
                    pass
                else:
                    result += calc(ul1, dr1, workflows[rule[3]], workflows)
                ul2_list = list(ul)
                ul2_list[coord_index] = rule[2]
                ul2 = cast(tuple[int, int, int, int], ul2_list)
                dr2 = dr
                print(f"for [{rule[2]},{dr[coord_index]}) [{ul2,dr2}) do next rule")
                result += calc(ul2, dr2, rules[1:], workflows)
            elif dr[0] <= rule[2]:
                if rule[3] == ACCEPT:
                    result += square(ul, dr)
                elif rule[3] == REJECT:
                    pass
                else:
                    result += calc(ul, dr, workflows[rule[3]], workflows)
            else:
                print(
                    f"rule[2] = {rule[2]} ul[{coord_index}] = {ul[coord_index]} dr[{coord_index}] = {dr[coord_index]}"
                )
                raise NotImplementedError
        elif rule[1] == GT:
            if rule[2] + 1 <= ul[coord_index]:
                raise NotImplementedError
            elif ul[coord_index] < rule[2] + 1 < dr[coord_index]:
                ul1 = ul
                dr1_list = list(dr)
                dr1_list[coord_index] = rule[2] + 1
                dr1 = cast(tuple[int, int, int, int], dr1_list)
                print(f"for [{ul[coord_index]},{rule[2]}) [{ul1,dr1}) do next rule")
                result += calc(ul1, dr1, rules[1:], workflows)
                ul2_list = list(ul)
                ul2_list[coord_index] = rule[2] + 1
                ul2 = cast(tuple[int, int, int, int], ul2_list)
                dr2 = dr
                print(f"for [{rule[2]},{dr[coord_index]}) [{ul2,dr2}) do {rule[3]}")
                if rule[3] == ACCEPT:
                    result += square(ul2, dr2)
                elif rule[3] == REJECT:
                    pass
                else:
                    result += calc(ul2, dr2, workflows[rule[3]], workflows)
            elif dr[coord_index] <= rule[2] + 1:
                raise NotImplementedError
            else:
                print(
                    f"rule[2] = {rule[2]} ul[{coord_index}] = {ul[coord_index]} dr[{coord_index}] = {dr[coord_index]}"
                )
                raise NotImplementedError
        else:
            print(f"rule[1] = {rule[1]}")
            raise NotImplementedError
    else:
        print(f"type(rule) = {type(rule)}")
        raise NotImplementedError
    return result


def main() -> None:
    workflows: dict[str, list[Rule]] = dict()
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                break
            name, rules_str = line[:-1].split("{")
            workflows[name] = []
            for rule_str in rules_str.split(","):
                if ":" in rule_str:
                    rule_match = re.match(r"^(\w+)([<>])(\d+):(\w+)$", rule_str)
                    if rule_match is None:
                        raise NotImplementedError
                    rule = rule_match.groups()
                    workflows[name].append((rule[0], rule[1], int(rule[2]), rule[3]))
                else:
                    workflows[name].append(rule_str)
    print(f"workflows = {workflows}")
    ul = (MIN_VALUE, MIN_VALUE, MIN_VALUE, MIN_VALUE)
    dr = (MAX_VALUE, MAX_VALUE, MAX_VALUE, MAX_VALUE)
    print(calc(ul, dr, workflows[START_WORKFLOW], workflows))


if __name__ == "__main__":
    main()
