from __future__ import annotations
from collections.abc import Iterator
import re

FILENAME = "demo.txt"  # expected 33
# FILENAME = "input.txt"

TIME_LIMIT = 24


class Minerals(tuple[int, int, int, int]):
    def __init__(self, *_: object) -> None:
        if len(self) != 4:
            raise NotImplementedError
        for i in range(4):
            if not isinstance(self[i], int):
                raise NotImplementedError

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Minerals):
            raise NotImplementedError
        return (
            self[0] < other[0] and self[1] < other[1] and self[2] < other[2] and self[2] < other[2]
        )

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Minerals):
            raise NotImplementedError
        return (
            self[0] > other[0] and self[1] > other[1] and self[2] > other[2] and self[3] > other[3]
        )

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Minerals):
            print(f"type(other) = {type(other)}")
            raise NotImplementedError
        return (
            self[0] >= other[0]
            and self[1] >= other[1]
            and self[2] >= other[2]
            and self[3] >= other[3]
        )

    def __add__(self, other: object) -> Minerals:
        if not isinstance(other, Minerals):
            raise NotImplementedError
        return Minerals(
            (self[0] + other[0], self[1] + other[1], self[2] + other[2], self[3] + other[3])
        )

    def __sub__(self, other: object) -> Minerals:
        if not isinstance(other, Minerals):
            raise NotImplementedError
        return Minerals(
            (self[0] - other[0], self[1] - other[1], self[2] - other[2], self[3] - other[3])
        )


class Blueprint:
    def __init__(
        self,
        ore_price: Minerals,
        clay_price: Minerals,
        obsidian_price: Minerals,
        geode_price: Minerals,
    ) -> None:
        self.ore_price = ore_price
        self.clay_price = clay_price
        self.obsidian_price = obsidian_price
        self.geode_price = geode_price

    def __repr__(self) -> str:
        return str((self.ore_price, self.clay_price, self.obsidian_price, self.geode_price))

    def calc(
        self, time_left: int, machines: Minerals, resources: Minerals, yesterday_resources: Minerals
    ) -> Iterator[tuple[Minerals, Minerals]]:
        if time_left < 0:
            raise NotImplementedError
        if time_left == 0:
            yield resources, machines
            return
        # Option 1: Just produce resources
        new_resources = resources + machines
        yield from self.calc(
            time_left=time_left - 1,
            machines=machines,
            resources=new_resources,
            yesterday_resources=resources,
        )
        # Option 2: Buy ore robot
        if resources >= self.ore_price and not (yesterday_resources >= self.ore_price):
            new_resources = resources + machines - self.ore_price
            new_machines = Minerals((machines[0] + 1, machines[1], machines[2], machines[3]))
            yield from self.calc(
                time_left=time_left - 1,
                machines=new_machines,
                resources=new_resources,
                yesterday_resources=resources,
            )
        # Option 3: Buy clay robot
        if resources >= self.clay_price and not (yesterday_resources >= self.clay_price):
            new_resources = resources + machines - self.clay_price
            new_machines = Minerals((machines[0], machines[1] + 1, machines[2], machines[3]))
            yield from self.calc(
                time_left=time_left - 1,
                machines=new_machines,
                resources=new_resources,
                yesterday_resources=resources,
            )
        # Option 4: Buy obsidian robot
        if resources >= self.obsidian_price and not (yesterday_resources >= self.obsidian_price):
            new_resources = resources + machines - self.obsidian_price
            new_machines = Minerals((machines[0], machines[1], machines[2] + 1, machines[3]))
            yield from self.calc(
                time_left=time_left - 1,
                machines=new_machines,
                resources=new_resources,
                yesterday_resources=resources,
            )
        # Option 5: Buy geode robot
        if resources >= self.geode_price and not (yesterday_resources >= self.geode_price):
            new_resources = resources + machines - self.geode_price
            new_machines = Minerals((machines[0], machines[1], machines[2], machines[3] + 1))
            yield from self.calc(
                time_left=time_left - 1,
                machines=new_machines,
                resources=new_resources,
                yesterday_resources=resources,
            )

    def get_best(self) -> int:
        result = 0
        for value in self.calc(
            time_left=TIME_LIMIT,
            machines=Minerals((1, 0, 0, 0)),
            resources=Minerals((0, 0, 0, 0)),
            yesterday_resources=Minerals((0, 0, 0, 0)),
        ):
            # print(f"value = {value}")
            if value[0][3] > result:
                result = value[0][3]
                print(f"value = {value}")
            # if value[0][3] == 5:
            #     print(f"value = {value}")
        return result


def main() -> None:
    current_blueprint_index = None
    current_ore_robot_cost = None
    current_clay_robot_cost = None
    current_obsidian_robot_cost = None
    current_geode_robot_cost = None
    blueprints: dict[int, Blueprint] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            blueprint_id_match = re.search(r"Blueprint (\d+):", line)
            if blueprint_id_match is not None:
                if current_blueprint_index is not None:
                    if (
                        current_ore_robot_cost is None
                        or current_clay_robot_cost is None
                        or current_obsidian_robot_cost is None
                        or current_geode_robot_cost is None
                    ):
                        raise NotImplementedError
                    blueprints[current_blueprint_index] = Blueprint(
                        current_ore_robot_cost,
                        current_clay_robot_cost,
                        current_obsidian_robot_cost,
                        current_geode_robot_cost,
                    )
                current_blueprint_index = int(blueprint_id_match.group(1))
                current_ore_robot_cost = None
                current_clay_robot_cost = None
                current_obsidian_robot_cost = None
                current_geode_robot_cost = None
            ore_robot_match = re.search(r"Each ore robot costs (\d+) ore", line)
            if ore_robot_match is not None:
                if current_ore_robot_cost is not None:
                    raise NotImplementedError
                current_ore_robot_cost = Minerals((int(ore_robot_match.group(1)), 0, 0, 0))
            clay_robot_match = re.search(r"Each clay robot costs (\d+) ore", line)
            if clay_robot_match is not None:
                if current_clay_robot_cost is not None:
                    raise NotImplementedError
                current_clay_robot_cost = Minerals((int(clay_robot_match.group(1)), 0, 0, 0))
            obsidian_robot_match = re.search(
                r"Each obsidian robot costs (\d+) ore and (\d+) clay", line
            )
            if obsidian_robot_match is not None:
                if current_obsidian_robot_cost is not None:
                    raise NotImplementedError
                current_obsidian_robot_cost = Minerals(
                    (
                        int(obsidian_robot_match.group(1)),
                        int(obsidian_robot_match.group(2)),
                        0,
                        0,
                    )
                )
            geode_robot_match = re.search(
                r"Each geode robot costs (\d+) ore and (\d+) obsidian", line
            )
            if geode_robot_match is not None:
                if current_geode_robot_cost is not None:
                    raise NotImplementedError
                current_geode_robot_cost = Minerals(
                    (
                        int(geode_robot_match.group(1)),
                        0,
                        int(geode_robot_match.group(2)),
                        0,
                    )
                )
    if (
        current_blueprint_index is None
        or current_ore_robot_cost is None
        or current_clay_robot_cost is None
        or current_obsidian_robot_cost is None
        or current_geode_robot_cost is None
    ):
        raise NotImplementedError
    blueprints[current_blueprint_index] = Blueprint(
        Minerals(current_ore_robot_cost),
        Minerals(current_clay_robot_cost),
        Minerals(current_obsidian_robot_cost),
        Minerals(current_geode_robot_cost),
    )
    print(blueprints)
    result = 0
    for index, blueprint in blueprints.items():
        result += index * blueprint.get_best()
        return
    print(result)


if __name__ == "__main__":
    main()
