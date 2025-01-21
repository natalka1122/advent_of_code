from __future__ import annotations
import re

FILENAME = "demo1.txt"  # expected 2
FILENAME = "input.txt"

OR = " | "
QUOTE = '"'
TARGET_RULE = 0


class Rule:
    def __init__(self, rule_str: str) -> None:
        if len(rule_str) == 3 and rule_str[0] == QUOTE and rule_str[2] == QUOTE:
            self.regex: str | None = rule_str[1]
            self.is_symbol = True
        else:
            self.regex = None
            self.rules_set: set[tuple[int, ...]] = set(
                map(
                    lambda x: tuple(map(int, x.split(" "))),
                    rule_str.split(OR),
                )
            )

    def check(self, line: str) -> bool:
        if self.regex is None:
            raise NotImplementedError
        return re.fullmatch(self.regex, line) is not None

    def __repr__(self) -> str:
        return str(self.__dict__)

    def clarify(self, the_rules: dict[int, Rule]) -> None:
        if self.regex is not None:
            return
        pre_regex: list[str] = []
        for rules in self.rules_set:
            pre_regex.append("")
            for rule_index in rules:
                if the_rules[rule_index].regex is None:
                    the_rules[rule_index].clarify(the_rules)
                current_regex = the_rules[rule_index].regex
                if current_regex is None:
                    raise NotImplementedError
                pre_regex[-1] += f"({current_regex})"
        if len(pre_regex) == 1:
            self.regex = pre_regex[0]
        self.regex = "(" + ")|(".join(pre_regex) + ")"


def main() -> None:
    the_rules: dict[int, Rule] = dict()
    is_rules = True
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                if not is_rules:
                    raise NotImplementedError
                is_rules = False
                the_rules[TARGET_RULE].clarify(the_rules)
            elif is_rules:
                name, rule = line.strip().split(": ")
                if int(name) in the_rules:
                    raise NotImplementedError
                the_rules[int(name)] = Rule(rule)
            else:
                if the_rules[TARGET_RULE].check(line.strip()):
                    result += 1
    print(result)


if __name__ == "__main__":
    main()
