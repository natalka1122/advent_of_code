import re

FILENAME = "input.txt"
AND = "AND"
OR = "OR"
XOR = "XOR"
Z = "z"


def main() -> None:
    def get_gate(a: str, operator: str, b: str) -> str:
        a, b = sorted([a, b])
        result = gates[(a, operator, b)]
        if result in nodes:
            return nodes[result]
        return result

    switches: set[tuple[str, str]] = {
        ("fph", "z15"),
        ("z21", "gds"),
        ("jrs", "wrk"),
        ("cqk", "z34"),
    }
    nodes: dict[str, str] = dict()
    for a, b in switches:
        nodes[a] = b
        nodes[b] = a
    gates: dict[tuple[str, str, str], str] = dict()
    is_inputs = True
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                if not is_inputs:
                    raise NotImplementedError
                is_inputs = False
            elif not is_inputs:
                gates_match = re.match(
                    "^([A-Za-z0-9]{3}) (OR|XOR|AND) ([A-Za-z0-9]{3}) -> ([A-Za-z0-9]{3})$",
                    line,
                )
                if gates_match is None:
                    raise NotImplementedError
                a, b = sorted([gates_match.group(1), gates_match.group(3)])
                gates[(a, gates_match.group(2), b)] = gates_match.group(4)
    print(f"gates = {gates}")
    print(f"nodes = {len(nodes)} {nodes}")
    # check x00 + y00 -> z00
    if gates[("x00", "XOR", "y00")] != "z00":
        raise NotImplementedError
    a = gates[("x00", "AND", "y00")]
    print(f"a = {a}")

    for i in range(1, 45):
        i_str = str(i).zfill(2)
        print(i_str)
        b = get_gate("x" + i_str, "AND", "y" + i_str)
        print(f"b = {b}")
        if b[0] in ["x", "y", "z"]:
            raise NotImplementedError
        c = get_gate("x" + i_str, "XOR", "y" + i_str)
        print(f"c = {c}")
        if c[0] in ["x", "y", "z"]:
            raise NotImplementedError
        z = get_gate(a, "XOR", c)
        if z != "z" + i_str:
            print(f"z = {z}")
            raise NotImplementedError
        d = get_gate(a, "AND", c)
        print(f"d = {d}")
        if d[0] in ["x", "y", "z"]:
            raise NotImplementedError
        a = get_gate(b, "OR", d)
        print(f"a = {a}")
        if a[0] in ["x", "y", "z"]:
            if i != 44:
                raise NotImplementedError
    print(",".join(sorted(nodes.values())))


if __name__ == "__main__":
    main()
