from __future__ import annotations
import re

FILENAME = "demo.txt"  # expected 6
FILENAME = "input.txt"

ZERO = "0"


class Program:
    def __init__(self, name: str, nei: set[Program] | None = None) -> None:
        self.name = name
        if nei is None:
            self.nei: set[Program] = set()
        else:
            self.nei = nei

    def is_connected(self, caller: set[Program]) -> bool:
        if self.name == ZERO:
            return True
        if self in caller:
            return False
        if any(map(lambda x: x.is_connected(caller.union({self})), self.nei)):
            return True
        return False


def main() -> None:
    programs: dict[str, Program] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"(\d+) <-> ([\d, ]+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            source = line_match.group(1)
            if source not in programs:
                programs[source] = Program(source)
            if len(programs[source].nei) > 0:
                raise NotImplementedError
            for nei in line_match.group(2).split(", "):
                if nei not in programs:
                    programs[nei] = Program(nei)
                programs[source].nei.add(programs[nei])
    result = 0
    for program in programs.values():
        if program.is_connected(set()):
            result += 1
    print(result)


if __name__ == "__main__":
    main()
