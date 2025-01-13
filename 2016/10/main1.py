from __future__ import annotations
import re

FILENAME, COMPARE_1, COMPARE_2 = "demo.txt", "value 002", "value 005"  # expected 2
FILENAME, COMPARE_1, COMPARE_2 = "input.txt", "value 017", "value 061"
MAX_LEN = 3


class Bot:
    # def __new__(cls, name: str) -> Bot | None:
    #     if name is None:
    #         return None
    #     return super(Bot, cls).__new__(cls)

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.numeric_inputs: set[str] = set()
        self.bot_inputs: set[Bot] = set()
        self.output1: Bot | None = None
        self.output2: Bot | None = None
        self.is_defined: bool = False
        self.is_processed: bool = False
        self.value1: str | None = None
        self.value2: str | None = None

    def __repr__(self) -> str:
        result = {
            "name": self.name,
            "numeric_inputs": self.numeric_inputs,
            "bot_inputs": set(
                map(lambda x: None if x is None else x.name, self.bot_inputs)
            ),
            "bot_outputs": (
                None if self.output1 is None else self.output1.name,
                None if self.output2 is None else self.output2.name,
            ),
            "values": (self.value1, self.value2),
            "is_defined": self.is_defined,
            "is_processed": self.is_processed,
        }
        return str(result)

    def __hash__(self) -> int:
        return hash(self.name)

    def get_values(self) -> tuple[str, str]:
        if (
            self.is_processed
            or not self.is_defined
            or self.value1 is None
            or self.value2 is None
        ):
            raise NotImplementedError
        self.is_processed = True
        return self.value1, self.value2

    def add_value(self, value: str) -> None:
        if self.is_defined or self.is_processed:
            print(f"Trying to add {value} to me {self}")
            raise NotImplementedError
        if len(self.numeric_inputs) >= 2:
            print(f"Trying to add {value} to me {self}")
            raise NotImplementedError
        if value in self.numeric_inputs:
            print(f"Trying to add {value} to me {self}")
            raise NotImplementedError
        self.numeric_inputs.add(value)
        if len(self.numeric_inputs) == 2:
            self.value1 = min(self.numeric_inputs)
            self.value2 = max(self.numeric_inputs)
            self.is_defined = True

    def add_outputs(self, bot1: Bot | None, bot2: Bot | None) -> None:
        if self.output1 is not None or self.output2 is not None:
            raise NotImplementedError
        self.output1 = bot1
        self.output2 = bot2


def main() -> None:
    bots: dict[str, Bot] = dict()
    instructions: list[tuple[str | None, ...]] = []
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            line_match1 = re.match(r"value (\d+) goes to bot (\d+)", line)
            if line_match1 is not None:
                bot_name = line_match1.group(2)
                bot_name = "bot " + "0" * (MAX_LEN - len(bot_name)) + bot_name
                if bot_name not in bots:
                    bots[bot_name] = Bot(bot_name)
                value = line_match1.group(1)
                value = "value " + "0" * (MAX_LEN - len(value)) + value
                bots[bot_name].add_value(value)
            else:
                line_match2 = re.match(
                    r"bot (\d+) gives low to (bot (\d+)|output (\d+)) and high to (bot (\d+)|output (\d)+)",
                    line,
                )
                if line_match2 is None:
                    raise NotImplementedError
                instructions.append(line_match2.groups()[:7])
    print("=== Got first data")
    for bot_name in sorted(bots):
        # if bots[str(bot_name)].is_processed:
        #     continue
        print(f"{bots[str(bot_name)]}")
    for instruction in instructions:
        bot_name = instruction[0]
        if bot_name is None:
            raise NotImplementedError
        bot_name = "bot " + "0" * (MAX_LEN - len(bot_name)) + bot_name
        if bot_name not in bots:
            bots[bot_name] = Bot(bot_name)
        # print(f"instruction = {instruction}")
        if instruction[2] is None:
            bot1 = None
        else:
            bot1_name = instruction[2]
            bot1_name = "bot " + "0" * (MAX_LEN - len(bot1_name)) + bot1_name
            if bot1_name not in bots:
                bots[bot1_name] = Bot(bot1_name)
            bot1 = bots[bot1_name]
        if instruction[5] is None:
            bot2 = None
        else:
            bot2_name = instruction[5]
            bot2_name = "bot " + "0" * (MAX_LEN - len(bot2_name)) + bot2_name
            if bot2_name not in bots:
                bots[bot2_name] = Bot(bot2_name)
            bot2 = bots[bot2_name]
        bots[bot_name].add_outputs(bot1, bot2)
    print("=== Added instructions")
    for bot_name in sorted(bots):
        # if bots[str(bot_name)].is_processed:
        #     continue
        print(f"{bots[str(bot_name)]}")
    changed_flag = True
    while changed_flag:
        changed_flag = False
        for bot_name in bots:
            if bots[bot_name].is_processed:
                continue
            if not bots[bot_name].is_defined:
                continue
            bot1 = bots[bot_name].output1
            bot2 = bots[bot_name].output2
            if bot1 is None or bot2 is None:
                continue
            value1, value2 = bots[bot_name].get_values()
            if (
                value1 is not None
                and value2 is not None
                and value1 == COMPARE_1
                and value2 == COMPARE_2
            ):
                print(f"bot_name = {bot_name}")
            if bot1 is not None:
                bot1.add_value(value1)
            if bot2 is not None:
                bot2.add_value(value2)
            changed_flag = True
            break
    # print("=== Finished")
    # for bot_name in sorted(bots):
    #     # if bots[str(bot_name)].is_processed:
    #     #     continue
    #     print(f"{bots[str(bot_name)]}")


if __name__ == "__main__":
    main()
