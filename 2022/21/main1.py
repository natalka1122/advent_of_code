FILENAME = "demo.txt"  # expected 152
FILENAME = "input.txt"

ADD = "+"
SUBSTRACT = "-"
MULIPLY = "*"
DIVIDE = "/"
ROOT = "root"


def f(n1: int, n2: int, op: str) -> int:
    if op == ADD:
        return n1 + n2
    if op == SUBSTRACT:
        return n1 - n2
    if op == MULIPLY:
        return n1 * n2
    if op == DIVIDE:
        return n1 // n2
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
        return str(self.__dict__)


def main() -> None:
    monkeys: dict[str, Monkey] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            name, job = line.strip().split(": ")
            if name in monkeys:
                raise NotImplementedError
            if job.isdigit():
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
            # print(name, monkey)
            if monkey.numbers is None or monkey.f is None:
                raise NotImplementedError
            monkey0_yell = monkeys[monkey.numbers[0]].yell
            monkey1_yell = monkeys[monkey.numbers[1]].yell
            if monkey0_yell is not None and monkey1_yell is not None:
                monkey.yell = f(
                    monkey0_yell,
                    monkey1_yell,
                    monkey.f,
                )
                in_cycle = False
        if in_cycle:
            print("I am broken")
            break
    print(monkeys[ROOT].yell)


if __name__ == "__main__":
    main()
