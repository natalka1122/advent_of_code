FILENAME = "demo.txt"  # expected 301
FILENAME = "input.txt"

ADD = "+"
SUBSTRACT = "-"
MULIPLY = "*"
DIVIDE = "/"
EQUAL = "="
ROOT = "root"
HUMN = "humn"


class NotEqual(Exception):
    pass


def f(op: str, n1: int, n2: int) -> int:
    if op == ADD:
        return n1 + n2
    if op == SUBSTRACT:
        return n1 - n2
    if op == MULIPLY:
        return n1 * n2
    if op == DIVIDE:
        return n1 // n2
    if op == EQUAL:
        if n1 == n2:
            return 0
        else:
            raise NotEqual
    raise NotImplementedError


def anti_f(op: str, result: int, n1: int | None = None, n2: int | None = None) -> int:
    if n1 is None and n2 is not None:
        if op == ADD:
            return result - n2
        if op == SUBSTRACT:
            return result + n2
        if op == MULIPLY:
            return result // n2
        if op == DIVIDE:
            return result * n2
        raise NotImplementedError
    if n1 is not None and n2 is None:
        if op == ADD:
            return result - n1
        if op == SUBSTRACT:
            return n1 - result
        if op == MULIPLY:
            return result // n1
        if op == DIVIDE:
            return n1 // result
        raise NotImplementedError
    raise NotImplementedError


class Monkey:
    def __init__(
        self,
        yell: int | None = None,
        f: str | None = None,
        numbers: list[str] | None = None,
    ) -> None:
        self.yell = yell
        self.f = f
        self.numbers = numbers

    def __repr__(self) -> str:
        result = []
        if self.yell is not None:
            result.append(str(self.yell))
        if self.numbers is not None:
            result.append(f"{self.numbers[0]} {self.f} {self.numbers[1]}")
        if len(result) == 0:
            return "HUMN"
        return " ".join(result)


def main() -> None:
    monkeys: dict[str, Monkey] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            name, job = line.strip().split(": ")
            if name in monkeys:
                raise NotImplementedError
            if name == ROOT:
                numbers = job.split(f" ")
                monkeys[name] = Monkey(numbers=[numbers[0], numbers[2]], f=EQUAL)
            elif name == HUMN:
                numbers = job.split(f" ")
                monkeys[name] = Monkey()
            elif job.isdigit():
                monkeys[name] = Monkey(yell=int(job))
            elif ADD in job:
                monkeys[name] = Monkey(numbers=job.split(f" {ADD} "), f=ADD)
            elif SUBSTRACT in job:
                monkeys[name] = Monkey(numbers=job.split(f" {SUBSTRACT} "), f=SUBSTRACT)
            elif MULIPLY in job:
                monkeys[name] = Monkey(numbers=job.split(f" {MULIPLY} "), f=MULIPLY)
            elif DIVIDE in job:
                monkeys[name] = Monkey(numbers=job.split(f" {DIVIDE} "), f=DIVIDE)
            else:
                raise NotImplementedError
    # print(monkeys)
    while monkeys["root"].yell is None:
        in_cycle = True
        for name, monkey in filter(lambda item: item[1].yell is None, monkeys.items()):
            if monkey.numbers is None or monkey.f is None:
                continue
            monkey0_yell = monkeys[monkey.numbers[0]].yell
            monkey1_yell = monkeys[monkey.numbers[1]].yell
            if monkey0_yell is not None and monkey1_yell is not None:
                try:
                    monkey.yell = f(
                        monkey.f,
                        monkey0_yell,
                        monkey1_yell,
                    )
                    in_cycle = False
                except NotEqual:
                    continue
        if in_cycle:
            break
    # print(monkeys)
    root_numbers = monkeys[ROOT].numbers
    if monkeys[ROOT].yell is not None or root_numbers is None:
        raise NotImplementedError
    if (
        monkeys[root_numbers[0]].yell is not None
        and monkeys[root_numbers[1]].yell is None
    ):
        current_monkey = root_numbers[1]
        current_value = monkeys[root_numbers[0]].yell
    elif (
        monkeys[root_numbers[0]].yell is None
        and monkeys[root_numbers[1]].yell is not None
    ):
        current_monkey = root_numbers[0]
        current_value = monkeys[root_numbers[1]].yell
    else:
        raise NotImplementedError
    monkeys[ROOT].yell = current_value
    # print(f"current_value = {current_value} current_monkey = {current_monkey}")
    while current_monkey != HUMN:
        current_numbers = monkeys[current_monkey].numbers
        current_f = monkeys[current_monkey].f
        if current_numbers is None or current_value is None or current_f is None:
            raise NotImplementedError
        if (
            monkeys[current_numbers[0]].yell is None
            and monkeys[current_numbers[1]].yell is not None
        ):
            next_value = anti_f(
                current_f,
                current_value,
                n2=monkeys[current_numbers[1]].yell,
            )
            next_monkey = current_numbers[0]
        elif (
            monkeys[current_numbers[0]].yell is not None
            and monkeys[current_numbers[1]].yell is None
        ):
            next_value = anti_f(
                current_f,
                current_value,
                n1=monkeys[current_numbers[0]].yell,
            )
            next_monkey = current_numbers[1]
        else:
            raise NotImplementedError
        monkeys[next_monkey].yell = next_value
        current_value = next_value
        current_monkey = next_monkey
        # print(f"current_value = {current_value} current_monkey = {current_monkey}")
        # print(monkeys)
    print(monkeys[HUMN])


if __name__ == "__main__":
    main()
