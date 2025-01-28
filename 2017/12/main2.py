from __future__ import annotations
import re

FILENAME = "demo.txt"  # expected 2
FILENAME = "input.txt"


class Program:
    def __init__(self, name: str, nei: set[Program] | None = None) -> None:
        self.name = name
        if nei is None:
            self.nei: set[Program] = set()
        else:
            self.nei = nei

    def __repr__(self) -> str:
        return f"Program({self.name})"

    def is_connected(self, source: Program, caller: set[Program]) -> bool:
        if self == source:
            return True
        if self in caller:
            return False
        if any(map(lambda x: x.is_connected(source, caller.union({self})), self.nei)):
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
            for nei in line_match.group(2).split(", "):
                if nei not in programs:
                    programs[nei] = Program(nei)
                programs[source].nei.add(programs[nei])
                programs[nei].nei.add(programs[source])
    groups = 0
    exclude: set[Program] = set()
    while len(exclude) < len(programs):
        groups += 1
        set_to_check = set(programs.values()) - exclude
        current: Program = set_to_check.pop()
        exclude.add(current)
        for program in set_to_check:
            if program.is_connected(current, set()):
                exclude.add(program)
    print(groups)


if __name__ == "__main__":
    main()
