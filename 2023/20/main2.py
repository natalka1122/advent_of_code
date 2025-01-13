from collections import OrderedDict
from collections.abc import Iterator
import re
from math import gcd

FILENAME = "input.txt"
START = "broadcaster"
RX = "rx"


def lcm(x, y):
    """Helper function to calculate the Least Common Multiple (LCM) of two numbers."""
    return abs(x * y) // gcd(x, y)


class Module:
    def __init__(
        self,
        line: str,
        is_broadcaster: bool = False,
        is_flipflop: bool = False,
        is_conjunction: bool = False,
    ) -> None:
        self.is_broadcaster = is_broadcaster
        self.is_flipflop = is_flipflop
        self.is_conjunction = is_conjunction
        self.next = line.split(", ") if line else []
        self.flipflop_state = False
        self.conjunction_state: OrderedDict[str, bool] = OrderedDict()

    def __repr__(self) -> str:
        return str(self.__dict__)

    def update_conjuction(self, input_module: str) -> None:
        if self.is_conjunction:
            self.conjunction_state[input_module] = False

    @property
    def state(self) -> tuple[bool, ...]:
        if self.is_broadcaster:
            return tuple()
        if self.is_flipflop:
            return (self.flipflop_state,)
        if self.is_conjunction:
            return tuple(self.conjunction_state.values())
        raise NotImplementedError

    def call(self, is_high: bool, input_module: str = "") -> tuple[bool, list[str]]:
        if self.is_broadcaster:
            return is_high, self.next
        if self.is_flipflop:
            if is_high:
                return (True, [])
            self.flipflop_state = not self.flipflop_state
            if self.flipflop_state:
                return (True, self.next)
            else:
                return (False, self.next)
        if self.is_conjunction:
            if not input_module:
                raise NotImplementedError
            if input_module not in self.conjunction_state:
                raise NotImplementedError
            self.conjunction_state[input_module] = is_high
            if all(self.state):
                return (False, self.next)
            return (True, self.next)
        raise NotImplementedError


def send_signal(
    start: str,
    is_high: bool,
    modules: dict[str, Module],
    caller: str,
    listen_for: tuple[str, ...],
) -> Iterator[int | None]:
    call_stack = [(start, is_high, caller)]
    while len(call_stack) > 0:
        current_name, current_high, current_caller = call_stack.pop(0)
        if current_name == RX and not current_high:
            raise NotImplementedError
        call_result = modules[current_name].call(
            is_high=current_high, input_module=current_caller
        )
        for elem in call_result[1]:
            if elem == RX and not call_result[0]:
                raise NotImplementedError
            if elem in listen_for and not call_result[0]:
                yield listen_for.index(elem)
            call_stack.append((elem, call_result[0], current_name))
    yield None


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
            if line_groups[1] is not None:
                modules[line_groups[1]] = Module(line_groups[6], is_broadcaster=True)
            elif line_groups[2] is not None:
                modules[line_groups[3]] = Module(line_groups[6], is_flipflop=True)
            elif line_groups[4] is not None:
                modules[line_groups[5]] = Module(line_groups[6], is_conjunction=True)
            else:
                raise NotImplementedError
    add_empty_modules = set()
    just_before_rx = None
    for name, module in modules.items():
        for next_module_name in module.next:
            if next_module_name in modules:
                modules[next_module_name].update_conjuction(name)
            else:
                add_empty_modules.add(next_module_name)
            if next_module_name == RX:
                if just_before_rx is not None:
                    raise NotImplementedError
                just_before_rx = name
    if just_before_rx is None:
        raise NotImplementedError
    if not modules[just_before_rx].is_conjunction:
        raise NotImplementedError
    for module_name in add_empty_modules:
        modules[module_name] = Module(line="", is_broadcaster=True)
    print(f"modules = {modules}")
    target_modules = modules[just_before_rx].conjunction_state.keys()
    print(target_modules)
    result = [[None, None] for _ in target_modules]
    i = 0
    states = set()
    for i in range(1, 20000):
        current_state = tuple(map(lambda x: modules[x].state, modules))
        if current_state in states:
            raise NotImplementedError
        states.add(current_state)
        for signal in send_signal(
            start=START,
            is_high=False,
            modules=modules,
            caller="button",
            listen_for=tuple(target_modules),
        ):
            if signal is None:
                continue
            if result[signal][0] is None:
                result[signal][0] = i
            elif result[signal][1] is None:
                if i == 2 * result[signal][0]:
                    result[signal] = [0, result[signal][0]]
                else:
                    result[signal][1] = i
            else:
                if i % result[signal][1] != result[signal][0]:
                    print(i, signal)
                    raise NotImplementedError
            print(result)
    if any(map(lambda x: x[0] != 0, result)):
        raise NotImplementedError
    print(lcm(lcm(lcm(result[0][1], result[1][1]), result[2][1]), result[3][1]))


if __name__ == "__main__":
    main()
