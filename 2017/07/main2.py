from __future__ import annotations
import re

FILENAME = "demo.txt"  # expected 60
FILENAME = "input.txt"


class Node:
    def __init__(self, name: str, weight: int | None = None) -> None:
        self.name = name
        self.my_weight = weight
        self.kids: set[Node] = set()
        self.parent: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.name})"

    @property
    def weight(self) -> int:
        if self.my_weight is None:
            raise NotImplementedError
        result: int = self.my_weight
        for kid in self.kids:
            result += kid.weight
        return result

    @property
    def is_balanced(self) -> bool:
        result = set()
        for kid in self.kids:
            result.add(kid.weight)
        return len(result) == 0 or len(result) == 1


def main() -> None:
    nodes: dict[str, Node] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"(\w+) \((\d+)\)( -> ([\w, ]+))?", line.strip())
            if line_match is None:
                print(line.strip())
                raise NotImplementedError
            node_name = line_match.group(1)
            node_weight = int(line_match.group(2))
            if node_name in nodes:
                nodes[node_name].my_weight = node_weight
            else:
                nodes[node_name] = Node(node_name, weight=node_weight)
            if line_match.group(3) is not None:
                for kid_node in line_match.group(4).split(", "):
                    if kid_node not in nodes:
                        nodes[kid_node] = Node(kid_node)
                    nodes[node_name].kids.add(nodes[kid_node])
                    nodes[kid_node].parent = nodes[node_name]

    candidates: set[Node] = set()
    for node in nodes.values():
        current_balance = node.is_balanced
        if not current_balance:
            candidates.add((node))
    print(candidates)
    not_candidates: set[Node] = set()
    is_changed = True
    while is_changed:
        is_changed = False
        for candidate1 in candidates - not_candidates:
            for candidate2 in candidates:
                if candidate1 == candidate2:
                    continue
                if candidate2 in candidate1.kids:
                    not_candidates.add(candidate1)
                    is_changed = True
                    break
            if is_changed:
                break

    if len(candidates - not_candidates) != 1:
        print(f"candidates = {candidates}")
        raise NotImplementedError
    unbalanced_node = (candidates - not_candidates).pop()
    print(unbalanced_node)
    kid_weights: dict[Node, int] = dict()
    for kid in unbalanced_node.kids:
        kid_weights[kid] = kid.weight
    proper_weight = 0
    troubled_kid = None
    troubled_weight = None
    for kid, kid_weight in kid_weights.items():
        if list(kid_weights.values()).count(kid_weight) == 1:
            troubled_kid = kid
            troubled_weight = kid_weight
        else:
            proper_weight = kid_weight
    if troubled_kid is None or troubled_weight is None or troubled_kid.my_weight is None:
        raise NotImplementedError
    print(troubled_kid.my_weight + proper_weight - troubled_weight)


if __name__ == "__main__":
    main()
