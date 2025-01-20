from __future__ import annotations
from collections.abc import Iterator
import re

FILENAME = "demo.txt"  # expected 33
# FILENAME = "input.txt"

TIME_LIMIT = 24


class NoResources(Exception):
    pass


class Minerals(tuple[int, int, int, int]):
    def __init__(self, *_: object) -> None:
        if len(self) != 4:
            raise NotImplementedError
        for i in range(4):
            if not isinstance(self[i], int):
                raise NotImplementedError
            if self[i] < 0:
                raise NoResources

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Minerals):
            raise NotImplementedError
        return (
            self[0] < other[0] and self[1] < other[1] and self[2] < other[2] and self[3] < other[3]
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

    def __mul__(self, other: object) -> Minerals:
        if not isinstance(other, int):
            raise NotImplementedError
        if other < 0:
            raise NotImplementedError
        if other == 0:
            return Minerals((0, 0, 0, 0))
        if other == 1:
            return self
        return self + self * (other - 1)


class State:
    def __init__(
        self,
        time_left: int,
        machines: Minerals,
        resources: Minerals,
        did_not_buy: Minerals,
        path: list[str],
    ) -> None:
        self.time_left = time_left
        self.machines = machines
        self.resources = resources
        self.did_not_buy = did_not_buy
        self.path = path

    def __repr__(self) -> str:
        return str(self.__dict__)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, State):
            raise NotImplementedError
        for i in [3, 2, 1, 0]:
            if self.resources[i] > other.resources[i]:
                return True
            if self.resources[i] < other.resources[i]:
                return False
            if self.machines[i] > other.machines[i]:
                return True
            if self.machines[i] < other.machines[i]:
                return False
        return self.time_left < other.time_left


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

    # def calc(
    #     self, time_left: int, machines: Minerals, resources: Minerals, yesterday_resources: Minerals
    # ) -> Iterator[tuple[Minerals, Minerals]]:
    #     if time_left < 0:
    #         raise NotImplementedError
    #     if time_left == 0:
    #         yield resources, machines
    #         return
    #     # Option 1: Just produce resources
    #     new_resources = resources + machines
    #     yield from self.calc(
    #         time_left=time_left - 1,
    #         machines=machines,
    #         resources=new_resources,
    #         yesterday_resources=resources,
    #     )
    #     # Option 2: Buy ore robot
    #     if resources >= self.ore_price and not (yesterday_resources >= self.ore_price):
    #         new_resources = resources + machines - self.ore_price
    #         new_machines = Minerals((machines[0] + 1, machines[1], machines[2], machines[3]))
    #         yield from self.calc(
    #             time_left=time_left - 1,
    #             machines=new_machines,
    #             resources=new_resources,
    #             yesterday_resources=resources,
    #         )
    #     # Option 3: Buy clay robot
    #     if resources >= self.clay_price and not (yesterday_resources >= self.clay_price):
    #         new_resources = resources + machines - self.clay_price
    #         new_machines = Minerals((machines[0], machines[1] + 1, machines[2], machines[3]))
    #         yield from self.calc(
    #             time_left=time_left - 1,
    #             machines=new_machines,
    #             resources=new_resources,
    #             yesterday_resources=resources,
    #         )
    #     # Option 4: Buy obsidian robot
    #     if resources >= self.obsidian_price and not (yesterday_resources >= self.obsidian_price):
    #         new_resources = resources + machines - self.obsidian_price
    #         new_machines = Minerals((machines[0], machines[1], machines[2] + 1, machines[3]))
    #         yield from self.calc(
    #             time_left=time_left - 1,
    #             machines=new_machines,
    #             resources=new_resources,
    #             yesterday_resources=resources,
    #         )
    #     # Option 5: Buy geode robot
    #     if resources >= self.geode_price and not (yesterday_resources >= self.geode_price):
    #         new_resources = resources + machines - self.geode_price
    #         new_machines = Minerals((machines[0], machines[1], machines[2], machines[3] + 1))
    #         yield from self.calc(
    #             time_left=time_left - 1,
    #             machines=new_machines,
    #             resources=new_resources,
    #             yesterday_resources=resources,
    #         )

    def get_best(self) -> int:
        result = 0
        Q: set[State] = {
            State(
                time_left=TIME_LIMIT,
                machines=Minerals((1, 0, 0, 0)),
                resources=Minerals((0, 0, 0, 0)),
                did_not_buy=Minerals((0, 0, 0, 0)),
                path=[],
            )
        }
        max_obsidian = 0
        while len(Q) > 0:
            current_state = None
            for state in Q:
                if current_state is None or current_state < state:
                    current_state = state
            Q.remove(current_state)
            if current_state.time_left < 0:
                raise NotImplementedError
            if current_state.time_left == 0:
                if current_state.resources[3] >= max_obsidian:
                    print(current_state)
                    max_obsidian = current_state.resources[3]
                continue
            max_ore_robot = 0
            if current_state.did_not_buy[0] == 0:
                while current_state.resources >= self.ore_price * (max_ore_robot + 1):
                    max_ore_robot += 1
            max_clay_robot = 0
            if current_state.did_not_buy[1] == 0:
                while current_state.resources >= self.clay_price * (max_clay_robot + 1):
                    max_clay_robot += 1
            max_obsidian_robot = 0
            if current_state.did_not_buy[2] == 0:
                while current_state.resources >= self.obsidian_price * (max_obsidian_robot + 1):
                    max_obsidian_robot += 1
            max_geode_robot = 0
            if current_state.did_not_buy[3] == 0:
                while current_state.resources >= self.geode_price * (max_geode_robot + 1):
                    max_geode_robot += 1
            # print(
            #     f"current_state.time_left = {current_state.time_left}",
            #     f"max_ore_robot = {max_ore_robot}",
            #     f"max_clay_robot = {max_clay_robot}",
            #     f"max_obsidian_robot = {max_obsidian_robot}",
            #     f"max_geode_robot = {max_geode_robot}",
            #     f"current_state = {current_state}",
            # )
            for buy_ore_robot in range(max_ore_robot + 1):
                for buy_clay_robot in range(max_clay_robot + 1):
                    for buy_obsidian_robot in range(max_obsidian_robot + 1):
                        for buy_geode_robot in range(max_geode_robot + 1):
                            did_not_buy_list = [
                                max(
                                    current_state.did_not_buy[0],
                                    max_ore_robot - buy_ore_robot,
                                ),
                                max(
                                    current_state.did_not_buy[1],
                                    max_clay_robot - buy_clay_robot,
                                ),
                                max(
                                    current_state.did_not_buy[2],
                                    max_obsidian_robot - buy_obsidian_robot,
                                ),
                                max(
                                    current_state.did_not_buy[3],
                                    max_geode_robot - buy_geode_robot,
                                ),
                            ]
                            if buy_ore_robot > 0:
                                did_not_buy_list[1] = 0
                                did_not_buy_list[2] = 0
                                did_not_buy_list[3] = 0
                            if buy_clay_robot > 0:
                                did_not_buy_list[0] = 0
                                did_not_buy_list[2] = 0
                                did_not_buy_list[3] = 0
                            if buy_obsidian_robot > 0:
                                did_not_buy_list[0] = 0
                                did_not_buy_list[1] = 0
                                did_not_buy_list[3] = 0
                            if buy_geode_robot > 0:
                                did_not_buy_list[0] = 0
                                did_not_buy_list[1] = 0
                                did_not_buy_list[2] = 0
                            try:
                                Q.add(
                                    State(
                                        time_left=current_state.time_left - 1,
                                        machines=Minerals(
                                            (
                                                current_state.machines[0] + buy_ore_robot,
                                                current_state.machines[1] + buy_clay_robot,
                                                current_state.machines[2] + buy_obsidian_robot,
                                                current_state.machines[3] + buy_geode_robot,
                                            )
                                        ),
                                        resources=current_state.resources
                                        + current_state.machines
                                        - self.ore_price * buy_ore_robot
                                        - self.clay_price * buy_clay_robot
                                        - self.obsidian_price * buy_obsidian_robot
                                        - self.geode_price * buy_geode_robot,
                                        did_not_buy=Minerals(did_not_buy_list),
                                        path=current_state.path
                                        + [
                                            (
                                                ""
                                                if buy_ore_robot == 0
                                                else f"buy {buy_ore_robot} ore_robot"
                                            )
                                            + (
                                                ""
                                                if buy_clay_robot == 0
                                                else f"buy {buy_clay_robot} clay_robot"
                                            )
                                            + (
                                                ""
                                                if buy_obsidian_robot == 0
                                                else f"buy {buy_obsidian_robot} obsidian_robot"
                                            )
                                            + (
                                                ""
                                                if buy_geode_robot == 0
                                                else f"buy {buy_geode_robot} geode_robot"
                                            )
                                        ],
                                    )
                                )
                            except NoResources:
                                continue
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
