from typing import Optional
import re

# FILENAME = "demo1_1.txt"  # expected 4
# FILENAME = "demo1_2.txt"  # expected 2024
FILENAME = "input.txt"
AND = "AND"
OR = "OR"
XOR = "XOR"
Z = "z"


def main():
    the_dict: dict[str, Optional[int]] = dict()
    gates: set[str, str, str, str] = set()
    is_inputs = True
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                if not is_inputs:
                    raise NotImplementedError
                is_inputs = False
            elif is_inputs:
                inputs_match = re.match("^([A-Za-z0-9]{3}): ([01])$", line)
                if inputs_match is None:
                    raise NotImplementedError
                key, value = inputs_match.groups()
                if key in the_dict:
                    raise NotImplementedError
                the_dict[key] = int(value)
            elif not is_inputs:
                gates_match = re.match(
                    "^([A-Za-z0-9]{3}) (OR|XOR|AND) ([A-Za-z0-9]{3}) -> ([A-Za-z0-9]{3})$",
                    line,
                )
                if gates_match is None:
                    raise NotImplementedError
                gates.add(gates_match.groups())
            else:
                raise NotImplementedError
    print(f"the_dict = {the_dict}")
    print(f"gates = {gates}")
    while gates:
        found = False
        for a, operand, b, c in gates:
            if a not in the_dict or b not in the_dict:
                continue
            found = True
            break
        if not found:
            raise NotImplementedError
        if c in the_dict:
            print(f"c = {c}")
            raise NotImplementedError
        print(a, operand, b, c)
        if operand == AND:
            the_dict[c] = the_dict[a] & the_dict[b]
        elif operand == OR:
            the_dict[c] = the_dict[a] or the_dict[b]
        elif operand == XOR:
            the_dict[c] = the_dict[a] ^ the_dict[b]
        else:
            raise NotImplementedError
        gates.remove((a, operand, b, c))

    z_keys = sorted(filter(lambda x: x.startswith(Z), the_dict.keys()), reverse=True)
    print(f"z_keys = {z_keys}")
    result = int("".join(list(map(lambda x: str(the_dict[x]), z_keys))), 2)
    print(f"result = {result}")


if __name__ == "__main__":
    main()
