from __future__ import annotations
from typing import Any
import re
import itertools

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

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Device):
            raise NotImplementedError
        return self.short_name < other.short_name

    def is_compatible(self, other: Device) -> bool:
        return (
            self.is_microchip
            and other.is_generator
            and self.short_name[0] == other.short_name[0]
        )


class NotValidFloor(Exception):
    pass


class Floor:
    def __init__(self, devices: list[Device] | None = None) -> None:
        if devices is None:
            self.devices = []
        else:
            for device in filter(lambda x: x.is_microchip, devices):
                no_generators_here = True
                my_generator_here = False
                for generator in filter(lambda x: x.is_generator, devices):
                    no_generators_here = False
                    if generator.type == device.type:
                        my_generator_here = True
                        break
                if not no_generators_here and not my_generator_here:
                    raise NotValidFloor
            self.devices = sorted(devices)
        self._str: str = str(self.devices)
        self.is_empty: bool = len(self.devices) == 0
        self._valid_moves: list[tuple[tuple[Device, ...], Floor]] | None = None

    @property
    def valid_moves(self) -> list[tuple[tuple[Device, ...], Floor]]:
        if self._valid_moves is not None:
            return self._valid_moves
        result: list[tuple[tuple[Device, ...], Floor]] = []
        for number in [1, 2]:
            for selected_devices in itertools.combinations(self.devices, number):
                new_floor_list: list[Device] = []
                for device in self.devices:
                    if device not in selected_devices:
                        new_floor_list.append(device)
                try:
                    new_floor: Floor = Floor(new_floor_list)
                except NotValidFloor:
                    continue
                result.append((selected_devices, new_floor))
        return result

    def __repr__(self) -> str:
        return self._str


class Building:
    def __init__(
        self, elevator: int = START, floors: list[Floor] | None = None
    ) -> None:
        self.elevator = elevator
        if floors is None:
            self.floors: list[Floor] = [Floor(), Floor(), Floor(), Floor()]
        else:
            self.floors = floors
        self._str = f"{self.elevator}: {self.floors}"
        self._hash = hash(self._str)

    def __repr__(self) -> str:
        return self._str

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Building):
            return False
        return self._str == self._str

    def __hash__(self) -> int:
        return self._hash

    def populate_floor(self, floor_number: int, devices: list[str]) -> None:
        if not self.floors[floor_number].is_empty:
            raise NotImplementedError
        self.floors[floor_number] = Floor(devices=list(map(Device, devices)))
        self._str = f"{self.elevator}: {self.floors}"
        self._hash = hash(self._str)

    @property
    def is_finite(self) -> bool:
        for index, floor in enumerate(self.floors):
            if index == TARGET:
                continue
            if not floor.is_empty:
                return False
        return True

    def valid_moves(self) -> list[Building]:
        result: list[Building] = []
        for selected_devices, source_floor in self.floors[self.elevator].valid_moves:
            new_floor_numbers = []
            if self.elevator > 0:
                new_floor_numbers.append(self.elevator - 1)
            if self.elevator < len(self.floors) - 1:
                new_floor_numbers.append(self.elevator + 1)
            for new_floor in new_floor_numbers:
                destination_floor_list = []
                for device in self.floors[new_floor].devices:
                    destination_floor_list.append(device)
                for device in selected_devices:
                    destination_floor_list.append(device)
                try:
                    destination_floor: Floor = Floor(destination_floor_list)
                except NotValidFloor:
                    continue
                new_building_floors = []
                for index, floor in enumerate(self.floors):
                    if index == self.elevator:
                        new_building_floors.append(source_floor)
                    elif index == new_floor:
                        new_building_floors.append(destination_floor)
                    else:
                        new_building_floors.append(floor)
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
            floor_number = INDEX[line.split(" ", 2)[1]]
            if floor_number == 0:
                line_split.extend(
                    [
                        "elerium generator",
                        "elerium-compatible microchip",
                        "dilithium generator",
                        "dilithium-compatible microchip",
                    ]
                )
            the_building.populate_floor(floor_number=floor_number, devices=line_split)
    print(f"the_building = {the_building}")
    # print(f"is_valid = {the_building.is_valid}")
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
        # if True:
            print(
                f"step = {step} current_building = {current_building} len(Q) = {len(Q)} len(visited) = {len(visited)}"
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
