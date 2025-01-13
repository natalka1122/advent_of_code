from __future__ import annotations
import re

# FILENAME = "demo.txt"
FILENAME = "input.txt"

START_WORKFLOW = "in"
ACCEPT = "A"
REJECT = "R"
X = "x"
M = "m"
A = "a"
S = "s"
LT = "<"
GT = ">"


def add_workflow(line: str, workflows) -> None:
    name, rules_str = line[:-1].split("{")
    rules = rules_str.split(",")
    for i in range(len(rules)):
        if ":" in rules[i]:
            rules[i] = re.match(r"^(\w+)([<>])(\d+):(\w+)$", rules[i]).groups()
    workflows[name] = rules


def process_part(part, start_workflow, workflows) -> int:
    x, m, a, s = map(int,re.match(r"^{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}$", part).groups())
    print(f"(x,m,a,s) = {(x,m,a,s)} start_workflow = {start_workflow} :: {workflows[start_workflow]}")
    for rule in workflows[start_workflow]:
        # print(f"rule = {rule}")
        if isinstance(rule, str):
            action = rule
            break
        else:
            action = None
            if rule[0] == X:
                value = x
            elif rule[0] == M:
                value = m
            elif rule[0] == A:
                value = a
            elif rule[0] == S:
                value = s
            else:
                raise NotImplementedError
            # print(f"value = {value} {rule[1]} {rule[2]}")
            if rule[1] == LT and value < int(rule[2]):
                action = rule[3]
                break
            if rule[1] == GT and value > int(rule[2]):
                action = rule[3]
                break
    # print(f"action = {action}")
    if action is None:
        raise NotImplementedError
    if action == ACCEPT:
        # print("ACCEPT")
        return x + m + a + s
    if action == REJECT:
        # print("REJECT")
        return 0
    return process_part(part, action, workflows)


def main():
    workflows = dict()
    result = 0
    with open(FILENAME, "r") as file:
        read_workflow = True
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                if not read_workflow:
                    raise NotImplementedError
                read_workflow = False
                print(f"workflows = {workflows}")
                continue
            if read_workflow:
                add_workflow(line, workflows)
            else:
                result += process_part(line, START_WORKFLOW, workflows)
    print(result)


if __name__ == "__main__":
    main()
