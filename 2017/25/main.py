FILENAME = "demo.txt"  # expected 3
FILENAME = "input.txt"

RIGHT = "right"


class Tape:
    def __init__(self) -> None:
        self._pos = 0
        self._value = {0: 0}

    def move_left(self) -> None:
        self._pos -= 1

    def move_right(self) -> None:
        self._pos += 1

    def get_value(self) -> int:
        if self._pos not in self._value:
            self._value[self._pos] = 0
        return self._value[self._pos]

    def set_value(self, n: int) -> None:
        if n not in [0, 1]:
            raise NotImplementedError
        self._value[self._pos] = n

    def count(self) -> int:
        return sum(self._value.values())


class State:
    def __init__(self) -> None:
        self.conditions: dict[int, tuple[int, bool, str]] = dict()

    def __repr__(self) -> str:
        return str(self.conditions)

    def add_condition(
        self, current_value: int, write_value: int, is_move_right: bool, next_state: str
    ) -> None:
        if current_value in self.conditions:
            raise NotImplementedError
        self.conditions[current_value] = write_value, is_move_right, next_state


def main() -> None:
    states: dict[str, State] = dict()
    start_state = None
    current_state = None
    current_value = None
    total_steps = None
    write_value = None
    is_move_right = None
    next_state = None
    with open(FILENAME, "r") as file:
        for line in file:
            if "Begin in state" in line:
                if start_state is not None:
                    raise NotImplementedError
                start_state = line.strip().split(" ")[-1][:-1]
            elif "Perform a diagnostic checksum after" in line:
                if total_steps is not None:
                    raise NotImplementedError
                total_steps = int(line.split(" ")[5])
            elif "In state" in line:
                if current_state is not None:
                    raise NotImplementedError
                current_state = line.strip().split(" ")[-1][:-1]
                states[current_state] = State()
            elif "If the current value is" in line:
                if current_value is not None:
                    raise NotImplementedError
                current_value = int(line.strip().split(" ")[-1][:-1])
            elif "Write the value" in line:
                if write_value is not None:
                    raise NotImplementedError
                write_value = int(line.strip().split(" ")[-1][:-1])
            elif "Move one slot to the" in line:
                if is_move_right is not None:
                    raise NotImplementedError
                is_move_right = line.strip().split(" ")[-1][:-1] == RIGHT
            elif "Continue with state" in line:
                if next_state is not None:
                    raise NotImplementedError
                next_state = line.strip().split(" ")[-1][:-1]
                if (
                    current_state is None
                    or current_value is None
                    or write_value is None
                    or is_move_right is None
                ):
                    raise NotImplementedError
                states[current_state].add_condition(
                    current_value, write_value, is_move_right, next_state
                )
                current_value = None
                write_value = None
                is_move_right = None
                next_state = None
            elif len(line.strip()) == 0:
                if current_state is not None:
                    current_state = None
                    if (
                        current_value is not None
                        or write_value is not None
                        or is_move_right is not None
                        or next_state is not None
                    ):
                        raise NotImplementedError
            else:
                raise NotImplementedError

    if start_state is None or total_steps is None:
        raise NotImplementedError
    print(f"start_state = {start_state}", f"total_steps = {total_steps}")
    print(states)
    current_state = start_state
    tape = Tape()
    for _ in range(total_steps):
        if current_state is None:
            raise NotImplementedError
        state = states[current_state]
        tape_value = tape.get_value()
        tape.set_value(state.conditions[tape_value][0])
        if state.conditions[tape_value][1]:
            tape.move_right()
        else:
            tape.move_left()
        current_state = state.conditions[tape_value][2]
    print(tape.count())


if __name__ == "__main__":
    main()
