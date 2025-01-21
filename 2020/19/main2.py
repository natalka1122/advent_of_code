from __future__ import annotations
from collections.abc import Iterator


FILENAME = "demo2.txt"  # expected 12
FILENAME = "input.txt"

OR = " | "
QUOTE = '"'
TARGET_RULE = 0
RULE8 = "8: 42 | 42 8"
RULE11 = "11: 42 31 | 42 11 31"


class Rule:
    def __init__(self, rule_str: str) -> None:
        if len(rule_str) == 3 and rule_str[0] == QUOTE and rule_str[2] == QUOTE:
            self.match: str | None = rule_str[1]
            self.is_symbol = True
        else:
            self.is_symbol = False
            self.rules_set: set[tuple[int, ...]] = set(
                map(
                    lambda x: tuple(map(int, x.split(" "))),
                    rule_str.split(OR),
                )
            )

    def check_part(self, line: str, the_rules: dict[int, Rule]) -> Iterator[int]:
        if self.is_symbol:
            if len(line) > 0 and line[0] == self.match:
                yield 1
            return
        for rules in self.rules_set:
            if len(rules) == 1:
                if isinstance(rules[0], int):
                    for line_add in the_rules[rules[0]].check_part(line, the_rules):
                        if line_add > len(line):
                            continue
                        yield line_add
                elif isinstance(rules[0], str):
                    raise NotImplementedError
                else:
                    raise NotImplementedError
            elif len(rules) == 2:
                for line_add0 in the_rules[rules[0]].check_part(line, the_rules):
                    if line_add0 >= len(line):
                        continue
                    for line_add1 in the_rules[rules[1]].check_part(line[line_add0:], the_rules):
                        if line_add0 + line_add1 > len(line):
                            continue
                        yield line_add0 + line_add1
            elif len(rules) == 3:
                for line_add0 in the_rules[rules[0]].check_part(line, the_rules):
                    if line_add0 >= len(line) - 1:
                        continue
                    for line_add1 in the_rules[rules[1]].check_part(line[line_add0:], the_rules):
                        if line_add0 + line_add1 >= len(line):
                            continue
                        for line_add2 in the_rules[rules[2]].check_part(
                            line[line_add0 + line_add1 :], the_rules
                        ):
                            if line_add0 + line_add1 + line_add2 > len(line):
                                continue
                            yield line_add0 + line_add1 + line_add2
            else:
                print(self.rules_set)
                raise NotImplementedError

    def check(self, line: str, the_rules: dict[int, Rule]) -> bool:
        for line_end in self.check_part(line, the_rules):
            if line_end == len(line):
                return True
        return False

    def __repr__(self) -> str:
        return str(self.__dict__)


def main() -> None:
    the_rules: dict[int, Rule] = dict()
    is_rules = True
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                if not is_rules:
                    raise NotImplementedError
                for rule_str in [RULE8, RULE11]:
                    name, rule = rule_str.split(": ")
                    the_rules[int(name)] = Rule(rule)
                is_rules = False
            elif is_rules:
                name, rule = line.strip().split(": ")
                if int(name) in the_rules:
                    raise NotImplementedError
                the_rules[int(name)] = Rule(rule)
            else:
                if the_rules[TARGET_RULE].check(line.strip(), the_rules):
                    result += 1
    print(result)


if __name__ == "__main__":
    main()
