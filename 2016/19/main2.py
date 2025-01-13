from __future__ import annotations

FILENAME = "demo.txt"  # expected 2
FILENAME = "demo2.txt"  # expected ?
FILENAME = "input.txt"


class Elf:
    def __init__(
        self, name: int, left_elf: Elf | None = None, right_elf: Elf | None = None
    ):
        self.name = name
        self.left: Elf | None = left_elf
        self.right: Elf | None = right_elf

    def __repr__(self):
        return str(self.name)

    def is_alone(self):
        return self.left is None and self.right is None


class ListOfElfes:
    def __init__(self, start: int, end: int):
        if end < start:
            self.first = None
            self.last = None
            self.length = 0
        elif start == end:
            self.first = Elf(start)
            self.last = self.first
            self.length = 1
        else:
            self.length = end - start + 1
            self.first = Elf(start)
            current = self.first
            for i in range(start + 1, end + 1):
                new_one = Elf(i, left_elf=current)
                current.right = new_one
                current = new_one
            self.last = current

    def __repr__(self) -> str:
        result = []
        current = self.first
        while current is not None:
            if current == self.first:
                if current.left is not None:
                    raise NotImplementedError
            elif current.left is None:
                raise NotImplementedError
            if current == self.last:
                if current.right is not None:
                    raise NotImplementedError
            elif current.right is None:
                raise NotImplementedError
            result.append(current)
            current = current.right
        return str(result)

    def add_to_right(self, elf: Elf) -> None:
        if not elf.is_alone():
            raise NotImplementedError
        if self.length == 0:
            self.first = elf
            self.last = elf
        else:
            self.last.right = elf
            elf.left = self.last
            self.last = elf
        self.length += 1

    def add_to_left(self, elf: Elf) -> None:
        if not elf.is_alone():
            raise NotImplementedError
        self.first.left = elf
        elf.right = self.first
        self.first = elf
        self.length += 1

    def pop_from_right(self) -> Elf:
        if self.length == 0:
            raise NotImplementedError
        if self.length == 1:
            result = self.first
            self.first = None
            self.last = None
        else:
            result = self.last
            self.last = self.last.left
            if self.last is not None:
                self.last.right = None
            result.left = None
        self.length -= 1
        if not result.is_alone():
            raise NotImplementedError
        return result

    def pop_from_left(self) -> Elf:
        if self.length == 0:
            raise NotImplementedError
        if self.length == 1:
            result = self.first
            self.first = None
            self.last = None
        else:
            result = self.first
            self.first = self.first.right
            if self.first is not None:
                self.first.left = None
            result.right = None
        self.length -= 1
        if not result.is_alone():
            raise NotImplementedError
        return result


def f(n: int) -> int:
    current = Elf(1)
    left = ListOfElfes(start=2, end=n // 2 + 1)
    right = ListOfElfes(start=n // 2 + 2, end=n)
    while left.length > 0 or right.length > 0:
        if left.length == right.length:
            left.pop_from_right()
            left.add_to_right(right.pop_from_left())
            right.add_to_right(current)
            left.add_to_right(right.pop_from_left())
            current = left.pop_from_left()
        elif left.length == right.length + 1:
            left.pop_from_right()
            if left.length == 0 and right.length == 0:
                break
            right.add_to_right(current)
            current = left.pop_from_left()
            left.add_to_right(right.pop_from_left())
        else:
            raise NotImplementedError
    return current.name


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(int(line)))


if __name__ == "__main__":
    main()
