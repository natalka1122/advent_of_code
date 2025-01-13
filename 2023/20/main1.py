from __future__ import annotations
from collections import OrderedDict
import re

# FILENAME = "demo1.txt"
# FILENAME = "demo2.txt"
FILENAME = "input.txt"
START = "broadcaster"
# PRESS_BUTTON = 1
PRESS_BUTTON = 1000


class Module:
    def __init__(
        self,
        line: str,
        is_broadcaster: bool = False,
        is_flipflop: bool = False,
        is_conjunction: bool = False,
    ) -> None:
        self._is_broadcaster = is_broadcaster
        self._is_flipflop = is_flipflop
        self._is_conjunction = is_conjunction
        self.next = line.split(", ") if line else []
        self._flipflop_state = False
        self._conjunction_state: OrderedDict[str, bool] = OrderedDict()

    def __repr__(self) -> str:
        return str(self.__dict__)

    def update_conjuction(self, input_module: str) -> None:
        if self._is_conjunction:
            self._conjunction_state[input_module] = False

    @property
    def state(self) -> tuple[bool, ...]:
        if self._is_broadcaster:
            return tuple()
        if self._is_flipflop:
            return (self._flipflop_state,)
        if self._is_conjunction:
            return tuple(self._conjunction_state.values())
        raise NotImplementedError

    def call(self, is_high: bool, input_module: str = "") -> tuple[bool, list[str]]:
        if self._is_broadcaster:
            return is_high, self.next
        if self._is_flipflop:
            if is_high:
                return (True, [])
            self._flipflop_state = not self._flipflop_state
            if self._flipflop_state:
                return (True, self.next)
            else:
                return (False, self.next)
        if self._is_conjunction:
            if not input_module:
                raise NotImplementedError
            if input_module not in self._conjunction_state:
                raise NotImplementedError
            self._conjunction_state[input_module] = is_high
            if all(self.state):
                return (False, self.next)
            return (True, self.next)
        raise NotImplementedError


def send_signal(
    start: str, is_high: bool, modules: dict[str, Module], caller: str
) -> tuple[int, int]:
    call_stack = [(start, is_high, caller)]
    result = [0, 0]
    while len(call_stack) > 0:
        current_name, current_high, current_caller = call_stack.pop(0)
        if current_high:
            result[0] += 1
        else:
            result[1] += 1
        # print(f"current_name = {current_name} current_high = {current_high} current_caller = {current_caller}")
        # print(
        #     f"{current_caller} {'-high' if current_high else '-low'} => {current_name}"
        # )
        call_result = modules[current_name].call(
            is_high=current_high, input_module=current_caller
        )
        # print(f"call_result = {call_result}")
        for elem in call_result[1]:
            call_stack.append((elem, call_result[0], current_name))
    return result


def main() -> None:
    modules: dict[str, Module] = dict()
    with open(FILENAME, "r") as file:
        for line_ in file:
            line_match = re.match(
                r"((broadcaster)|(%)(\w+)|(&)(\w+))\s->\s(\w+(,\s\w+)*)", line_.strip()
            )
            if line_match is None:
                raise NotImplementedError
            line_groups = line_match.groups()
            # print(line_groups)
            if line_groups[1] is not None:
                modules[line_groups[1]] = Module(line_groups[6], is_broadcaster=True)
            elif line_groups[2] is not None:
                modules[line_groups[3]] = Module(line_groups[6], is_flipflop=True)
            elif line_groups[4] is not None:
                modules[line_groups[5]] = Module(line_groups[6], is_conjunction=True)
            else:
                raise NotImplementedError
    # print(modules)
    add_empty_modules = set()
    for name, module in modules.items():
        for next_module_name in module.next:
            if next_module_name in modules:
                modules[next_module_name].update_conjuction(name)
            else:
                add_empty_modules.add(next_module_name)
    for module_name in add_empty_modules:
        modules[module_name] = Module(line="", is_broadcaster=True)
    print(f"modules = {modules}")
    result = [0, 0]
    for i in range(PRESS_BUTTON):
        print(i)
        # current_state = tuple(map(lambda x: modules[x].state, modules))
        # print(f"current_state = {current_state}")
        high_sent, low_sent = send_signal(
            start=START, is_high=False, modules=modules, caller="button"
        )
        print(f"high_sent = {high_sent} low_sent = {low_sent}")
        result[0] += high_sent
        result[1] += low_sent
    print(result[0] * result[1])


if __name__ == "__main__":
    main()
