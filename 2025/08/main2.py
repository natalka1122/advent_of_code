from dataclasses import dataclass

# FILENAME = "demo.txt"  # expected 25272
FILENAME = "input.txt"


@dataclass
class Box:
    x: int
    y: int
    z: int

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def dist(self, box: "Box") -> int:
        return (self.x - box.x) ** 2 + (self.y - box.y) ** 2 + (self.z - box.z) ** 2


class Circuit:
    def __init__(self, box: Box) -> None:
        self.boxes = set([box])

    def __len__(self) -> int:
        return len(self.boxes)

    def add(self, box: Box) -> None:
        if box in self.boxes:
            raise NotImplementedError
        self.boxes.add(box)


def main() -> None:
    boxes: set[Box] = set()
    circuits: set[Circuit] = set()
    box_to_cirquit: dict[Box, Circuit] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            box = Box(*tuple(map(int, line.strip().split(","))))
            boxes.add(box)
            circuit = Circuit(box)
            circuits.add(circuit)
            box_to_cirquit[box] = circuit

    distances: dict[tuple[Box, Box], int] = dict()
    distances_list: list[tuple[int, Box, Box]] = []
    for b1 in boxes:
        for b2 in boxes:
            if b1 == b2 or (b2, b1) in distances:
                continue
            d = b1.dist(b2)
            distances[b1, b2] = d
            distances_list.append((d, b1, b2))
    distances_list.sort(key=lambda x: x[0])
    index = 0
    while len(circuits) > 1:
        b1, b2 = distances_list[index][1:]
        c1 = box_to_cirquit[b1]
        c2 = box_to_cirquit[b2]
        if c1 == c2:
            index += 1
            continue
        for box in c2.boxes:
            c1.add(box)
            box_to_cirquit[box] = c1
        circuits.remove(c2)
        if len(circuits) == 1:
            print(b1.x * b2.x)
            return
        box_to_cirquit[b2] = c1
        index += 1


if __name__ == "__main__":
    main()
