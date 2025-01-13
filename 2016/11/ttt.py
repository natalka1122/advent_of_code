from __future__ import annotations
from typing import Any
import re
import itertools

FILENAME = "demo.txt"  # expected 11
FILENAME = "input.txt"
INDEX = {"first": 0, "second": 1, "third": 2, "fourth": 3}
TARGET = 3
START = 0
MICROCHIP = "M"
GENERATOR = "G"


class Device:
    def __init__(self, name: str) -> None:
        self.name = name
        self.short_name = "".join(map(lambda x: x[0].upper(), name.split(" ")))
        self.is_microchip = self.short_name[1] == MICROCHIP
        self.is_generator = self.short_name[1] == GENERATOR
        self.type = self.short_name[0]

    def __repr__(self) -> str:
        return self.short_name

    def is_compatible(self, other: Device) -> bool:
        return (
            self.is_microchip
            and other.is_generator
            and self.short_name[0] == other.short_name[0]
        )


def is_valid_floor(floor: set[Device]) -> bool:
    for device in filter(lambda x: x.is_microchip, floor):
        no_generators_here = True
        my_generator_here = False
        for generator in filter(lambda x: x.is_generator, floor):
            no_generators_here = False
            if generator.type == device.type:
                my_generator_here = True
                break
        if not no_generators_here and not my_generator_here:
            return False
    return True


class Building:
    def __init__(
        self, elevator: int = START, floors: list[set[Device]] | None = None
    ) -> None:
        self.elevator = elevator
        if floors is None:
            self.floors: list[set[Device]] = [set(), set(), set(), set()]
        else:
            self.floors = floors
        if not self.is_valid:
            raise NotImplementedError

    def __repr__(self) -> str:
        return str(self.floors)

    def __str__(self) -> str:
        return f"{self.elevator}: {self.floors}"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Building):
            return False
        return str(self) == str(other)

    def __hash__(self) -> int:
        return hash(str(self))

    def populate_floor(self, floor_number: int, devices: list[str]) -> None:
        if len(self.floors[floor_number]) != 0:
            raise NotImplementedError
        self.floors[floor_number] = set(map(Device, devices))
        if not is_valid_floor(self.floors[floor_number]):
            raise NotImplementedError

    @property
    def is_finite(self) -> bool:
        for key, value in enumerate(self.floors):
            if key == TARGET:
                continue
            if len(value) != 0:
                return False
        return True

    @property
    def is_valid(self) -> bool:
        for floor in self.floors:
            if not is_valid_floor(floor):
                return False
        return True

    def valid_moves(self) -> list[Building]:
        result: list[Building] = []
        for number in [1, 2]:
            for selected_devices in itertools.combinations(
                self.floors[self.elevator], number
            ):
                source_floor = set()
                for device in self.floors[self.elevator]:
                    if device not in selected_devices:
                        source_floor.add(device)
                if not is_valid_floor(source_floor):
                    continue
                new_floor_numbers = []
                if self.elevator > 0:
                    new_floor_numbers.append(self.elevator - 1)
                if self.elevator < len(self.floors) - 1:
                    new_floor_numbers.append(self.elevator + 1)
                for new_floor in new_floor_numbers:
                    destination_floor = set()
                    for device in self.floors[new_floor]:
                        destination_floor.add(device)
                    for device in selected_devices:
                        destination_floor.add(device)
                    if not is_valid_floor(destination_floor):
                        continue
                    new_building_floors = []
                    for index, floor in enumerate(self.floors):
                        if index == self.elevator:
                            new_building_floors.append(source_floor)
                        elif index == new_floor:
                            new_building_floors.append(destination_floor)
                        else:
                            new_building_floors.append(set(floor))
                    new_building = Building(new_floor, new_building_floors)
                    result.append(new_building)
        return result


def main() -> None:
    the_building = Building()
    with open(FILENAME, "r") as file:
        for line in file:
            line_split = re.findall(
                r"([a-z]+ generator|[a-z]+-compatible microchip)", line
            )
            the_building.populate_floor(
                floor_number=INDEX[line.split(" ", 2)[1]], devices=line_split
            )
    print(f"the_building = {the_building}")
    print(f"is_valid = {the_building.is_valid}")
    print(f"is_finite = {the_building.is_finite}")
    print(f"valid_moves = {the_building.valid_moves()}")
    print(f"the_building = {the_building}")
    Q = [(0, the_building)]
    visited: set[Building] = {the_building}
    found_it = False
    prev_step = 0
    while not found_it and len(Q) > 0:
        step, current_building = Q.pop(0)
        if step != prev_step:
            print(
                f"step = {step} current_building = {current_building} len(Q) = {len(Q)}"
            )
            prev_step = step
        for next_building in current_building.valid_moves():
            if next_building in visited:
                continue
            if next_building.is_finite:
                print(f"step = {step+1}")
                found_it = True
                break
            else:
                Q.append((step + 1, next_building))
                visited.add(next_building)


if __name__ == "__main__":
    main()
