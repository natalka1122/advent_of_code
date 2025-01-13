import re

FILENAME, COMPARE_1, COMPARE_2 = "demo.txt", "value 2", "value 5"  # expected 2
FILENAME, COMPARE_1, COMPARE_2 = "input.txt", "value 17", "value 61"
INPUTS = "inputs"
GOES_TO = "goes_to"


class Bot:
    def __init__(self) -> None:
        self._inputs: set[str] = set()
        self.goes_to: tuple[str | None, str | None] | None = None
        self.done = False

    def __repr__(self) -> str:
        return str(self.__dict__)

    def clear_values(self) -> None:
        self._inputs = set()
        self.done = True

    def add_value(self, value: str) -> None:
        if self.done:
            raise NotImplementedError
        if len(self._inputs) >= 2:
            raise NotImplementedError
        if value in self._inputs:
            raise NotImplementedError
        self._inputs.add(value)
        if len(self._inputs) == 2:
            self.values = tuple(sorted(self._inputs))

    def define(self, value1: str | None, value2: str | None) -> None:
        if self.goes_to is not None:
            raise NotImplementedError
        self.goes_to = value1, value2
        if value1 is None and value2 is None:
            self.done = True

    @property
    def is_ready(self) -> bool:
        return len(self._inputs) == 2


def main() -> None:
    bots: dict[str, Bot] = dict()
    found_flag = False
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            line_match1 = re.match(r"(value \d+) goes to bot (\d+)", line)
            if line_match1 is not None:
                bot_name = line_match1.group(2)
                if bot_name not in bots:
                    bots[bot_name] = Bot()
                bots[bot_name].add_value(line_match1.group(1))
            else:
                line_match2 = re.match(
                    r"bot (\d+) gives low to (bot (\d+)|output (\d)+) and high to (bot (\d+)|output (\d)+)",
                    line,
                )
                if line_match2 is None:
                    raise NotImplementedError
                bot_name = line_match2.group(1)
                if bot_name not in bots:
                    bots[bot_name] = Bot()
                bots[bot_name].define(line_match2.group(3), line_match2.group(6))
            changed_flag = True
            while changed_flag:
                changed_flag = False
                for bot_name in bots:
                    if not bots[bot_name].is_ready:
                        continue
                    if bots[bot_name].goes_to is None:
                        continue
                    values = bots[bot_name].values
                    if values[0] == COMPARE_1 and values[1] == COMPARE_2:
                        print(f"bot_name = {bot_name}")
                        # found_flag = True
                        # break
                    for index, target in enumerate(bots[bot_name].goes_to):
                        if target is None:
                            continue
                        if target not in bots:
                            bots[target] = Bot()
                        bots[target].add_value(values[index])
                        changed_flag = True
                    if found_flag:
                        break
                    if changed_flag:
                        bots[bot_name].clear_values()
                        break
                if found_flag:
                    break
            if found_flag:
                break
    for bot_name in bots:
        if bots[bot_name].done:
            continue
        print(f"{bot_name}: {bots[bot_name]}")


if __name__ == "__main__":
    main()
