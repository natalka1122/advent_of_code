from __future__ import annotations
from queue import SimpleQueue

FILENAME = "demo1_1.txt"  # expected ?
FILENAME = "demo1_2.txt"  # expected 27730
# FILENAME = "demo1_3.txt"  # expected 36334
# FILENAME = "demo1_4.txt"  # expected 27755
# FILENAME = "demo1_5.txt"  # expected 28944
# FILENAME = "demo1_6.txt"  # expected 18740
# FILENAME = "demo1_10.txt"  # expected ???
# FILENAME = "demo1_11.txt"  # expected ???
# FILENAME = "demo1_12.txt"  # expected ???
# FILENAME = "demo1_13.txt"  # expected ???
# FILENAME = "input.txt"

ELF = "E"
GOBLIN = "G"
EMPTY = "."
WALL = "#"
ATTACK_POWER = 3
HIT_POINTS = 200
DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


class Hero:
    def __init__(self, y: int, x: int, is_elf: bool, the_map: list[list[bool]]):
        self.y = y
        self.x = x
        self.attack_power = ATTACK_POWER
        self.hit_points = HIT_POINTS
        self.the_map = the_map
        self.is_elf = is_elf

    def __repr__(self) -> str:
        if self.is_elf:
            return f"Elf({self.y}, {self.x})"
        else:
            return f"Goblin({self.y}, {self.x})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hero):
            raise NotImplementedError
        return (self.y, self.x) == (other.y, other.x)

    def __hash__(self) -> int:
        return hash((self.y, self.x))

    def attack(self, other: Hero) -> bool:
        other.hit_points -= self.attack_power
        if other.hit_points <= 0:
            self.the_map[other.y][other.x] = True
            return True
        return False

    def move(self, y: int, x: int) -> None:
        if self.the_map[self.y][self.x]:
            raise NotImplementedError
        self.the_map[self.y][self.x] = True
        if not self.the_map[y][x]:
            raise NotImplementedError
        self.y = y
        self.x = x
        self.the_map[self.y][self.x] = False


def show_map(heroes: dict[tuple[int, int], Hero], the_map: list[list[bool]]) -> None:
    for y in range(len(the_map)):
        mentioned_heroes = []
        for x in range(len(the_map[0])):
            if the_map[y][x]:
                symbol = EMPTY
            elif not the_map[y][x]:
                if (y, x) in heroes:
                    symbol = ELF if heroes[y, x].is_elf else GOBLIN
                    mentioned_heroes.append(f"{symbol}({heroes[y, x].hit_points})")
                else:
                    symbol = WALL
            else:
                raise NotImplementedError
            print(symbol, end="")
        print("  ", ", ".join(mentioned_heroes))


def find_targets(hero: Hero, heroes: dict[tuple[int, int], Hero]) -> set[Hero]:
    targets: set[Hero] = set()
    for enemy_hero in heroes.values():
        if enemy_hero.hit_points <= 0 or hero.is_elf == enemy_hero.is_elf:
            continue
        targets.add(enemy_hero)
    return targets


def find_can_attack(hero: Hero, targets: set[Hero]) -> set[tuple[int, int]]:
    target_coords = {(h.y, h.x) for h in targets}
    result: set[tuple[int, int]] = set()
    for dy, dx in DIRECTIONS:
        if (hero.y + dy, hero.x + dx) in target_coords:
            result.add((hero.y + dy, hero.x + dx))
    return result


def find_attack_target(
    can_attack: set[tuple[int, int]], heroes: dict[tuple[int, int], Hero]
) -> tuple[int, int]:
    min_health = None
    min_health_coords = set()
    for coord in can_attack:
        if coord not in heroes:
            raise NotImplementedError
        if min_health is None or min_health > heroes[coord].hit_points:
            min_health = heroes[coord].hit_points
            min_health_coords = {coord}
        elif min_health == heroes[coord].hit_points:
            min_health_coords.add(coord)
    if min_health is None:
        raise NotImplementedError
    return min(min_health_coords)


def find_in_range(targets: set[Hero], the_map: list[list[bool]]) -> set[tuple[int, int]]:
    result: set[tuple[int, int]] = set()
    for hero in targets:
        for dy, dx in DIRECTIONS:
            if the_map[hero.y + dy][hero.x + dx]:
                result.add((hero.y + dy, hero.x + dx))
    return result


def find_reachable(
    hero: Hero, in_range: set[tuple[int, int]], the_map: list[list[bool]]
) -> dict[tuple[int, int], tuple[int, set[tuple[int, int]]]]:
    found_paths: dict[tuple[int, int], tuple[int, set[tuple[int, int]]]] = {}
    Q: SimpleQueue[tuple[int, int]] = SimpleQueue()
    for dy, dx in DIRECTIONS:
        y = hero.y + dy
        x = hero.x + dx
        if the_map[y][x]:
            Q.put((y, x))
            found_paths[y, x] = 1, {(y, x)}
    while not Q.empty():
        # print(Q.qsize())
        y0, x0 = Q.get()
        for dy, dx in DIRECTIONS:
            y = y0 + dy
            x = x0 + dx
            # if (y, x) in in_range:
            #     continue
            if not the_map[y][x]:
                continue
            # if (y, x) in visited:
            #     continue
            if (y, x) not in found_paths or found_paths[y, x][0] > found_paths[y0, x0][0] + 1:
                found_paths[y, x] = found_paths[y0, x0][0] + 1, found_paths[y0, x0][1]
                if len(found_paths[y, x][1]) == 0:
                    raise NotImplementedError
                Q.put((y, x))
            elif found_paths[y, x][0] == found_paths[y0, x0][0] + 1:
                prev_path_count = len(found_paths[y, x][1])
                for path in found_paths[y0, x0][1]:
                    found_paths[y, x][1].add(path)
                current_path_count = len(found_paths[y, x][1])
                if current_path_count > prev_path_count:
                    Q.put((y, x))
                    # print(f"current_path_count = {current_path_count}")
                    if current_path_count > 1000:
                        print(found_paths[y, x])
                        raise NotImplementedError
    # print(f"found_paths = {found_paths}")
    result: dict[tuple[int, int], tuple[int, set[tuple[int, int]]]] = {}
    for y, x in in_range:
        if (y, x) in found_paths:
            result[y, x] = found_paths[y, x]
    return result


def find_nearest(
    reachable: dict[tuple[int, int], tuple[int, set[tuple[int, int]]]]
) -> dict[tuple[int, int], set[tuple[int, int]]]:
    result: dict[tuple[int, int], set[tuple[int, int]]] = {}
    best_distance = min(map(lambda x: x[0], reachable.values()))
    # print(f"best_distance = {best_distance}")
    for key, value in reachable.items():
        if value[0] == best_distance:
            result[key] = value[1]
    return result


def find_chosen(nearest: dict[tuple[int, int], set[tuple[int, int]]]) -> set[tuple[int, int]]:
    result = None
    for key, value in nearest.items():
        if result is None or nearest[result] > value:
            result = key
    if result is None:
        raise NotImplementedError
    return nearest[result]


def find_step(chosen: set[tuple[int, int]]) -> tuple[int, int]:
    return min(chosen)


def main() -> None:
    the_map: list[list[bool]] = []
    heroes: dict[tuple[int, int], Hero] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append([])
            y = len(the_map) - 1
            for x in range(len(line)):
                if line[x] == WALL:
                    the_map[-1].append(False)
                elif line[x] == EMPTY:
                    the_map[-1].append(True)
                elif line[x] == ELF:
                    if (y, x) in heroes:
                        raise NotImplementedError
                    heroes[y, x] = Hero(y, x, is_elf=True, the_map=the_map)
                    the_map[-1].append(False)
                elif line[x] == GOBLIN:
                    if (y, x) in heroes:
                        raise NotImplementedError
                    heroes[y, x] = Hero(y, x, is_elf=False, the_map=the_map)
                    the_map[-1].append(False)
                elif line[x] != "\n":
                    raise NotImplementedError
    show_map(heroes, the_map)
    step_count = 0
    combat_ends = False
    while not combat_ends:
        # print(f"step_count = {step_count}")
        sorted_heroes = sorted(heroes)
        for hero_y, hero_x in sorted_heroes:
            hero = heroes[hero_y, hero_x]
            if hero.hit_points <= 0:
                continue
            # print(f"{hero}")
            # print(f"{hero}", end=" ")
            targets: set[Hero] = find_targets(hero=hero, heroes=heroes)
            # print(f"targets = {targets}")
            if len(targets) == 0:
                print("combat ends")
                combat_ends = True
                break
            can_attack = find_can_attack(hero, targets)
            # print(f"can_attack = {can_attack}")
            if len(can_attack) == 0:
                in_range: set[tuple[int, int]] = find_in_range(targets, the_map)
                # print(f"in_range = {in_range}")
                if len(in_range) == 0:
                    # print("nothing to do")
                    continue
                if (hero.y, hero.x) in in_range:
                    print("not possible")
                    raise NotImplementedError
                else:
                    reachable = find_reachable(hero, in_range, the_map)
                    # print(f"reachable = {reachable}")
                    if len(reachable) > 0:
                        nearest = find_nearest(reachable)
                        # print(f"nearest = {nearest}")
                        chosen = find_chosen(nearest)
                        # print(f"chosen = {chosen}")
                        next_step = find_step(chosen)
                        # print(f"next_step = {next_step}")
                        # print(f"move to {next_step}")
                        del heroes[hero.y, hero.x]
                        hero.move(next_step[0], next_step[1])
                        heroes[next_step] = hero
                        can_attack = find_can_attack(hero, targets)
            if len(can_attack) > 0:
                attack_target = find_attack_target(can_attack, heroes)
                # print(f"attack {attack_target}")
                hero.attack(heroes[attack_target])
        show_map(heroes, the_map)
        if combat_ends:
            break
        step_count += 1
    outcome = 0
    for hero in heroes.values():
        if hero.hit_points >= 0:
            outcome += hero.hit_points
    show_map(heroes, the_map)
    print(step_count, outcome)
    print(step_count * outcome)


if __name__ == "__main__":
    main()
