from __future__ import annotations
import itertools

FILENAME, MY_HIT_POINTS, MY_DAMAGE, MY_ARMOR = "demo.txt", 8, 5, 5  # expected 0
FILENAME, MY_HIT_POINTS, MY_DAMAGE, MY_ARMOR = "input.txt", 100, 0, 0

WEAPONS = {
    "Empty_weapon": (0, 0, 0),
    "Dagger": (8, 4, 0),
    "Shortsword": (10, 5, 0),
    "Warhammer": (25, 6, 0),
    "Longsword": (40, 7, 0),
    "Greataxe": (74, 8, 0),
}
ARMOR = {
    "Empty_armor": (0, 0, 0),
    "Leather": (13, 0, 1),
    "Chainmail": (31, 0, 2),
    "Splintmail": (53, 0, 3),
    "Bandedmail": (75, 0, 4),
    "Platemail": (102, 0, 5),
}

RINGS = {
    "Empty_ring_1": (0, 0, 0),
    "Empty_ring_2": (0, 0, 0),
    "Damage +1": (25, 1, 0),
    "Damage +2": (50, 2, 0),
    "Damage +3": (100, 3, 0),
    "Defense +1": (20, 0, 1),
    "Defense +2": (40, 0, 2),
    "Defense +3": (80, 0, 3),
}


class Hero:
    def __init__(self, hit_point: int, damage: int, armor: int) -> None:
        self.hit_point = hit_point
        self.damage = damage
        self.armor = armor

    def fight(self, other: Hero, equip: list[tuple[int, int, int]]) -> bool:
        self_hit_points = self.hit_point
        other_hit_points = other.hit_point
        self_damage = self.damage + sum(map(lambda x: x[1], equip))
        self_armor = self.armor + sum(map(lambda x: x[2], equip))
        while self_hit_points > 0 and other_hit_points > 0:
            other_hit_points -= max(1, self_damage - other.armor)
            if other_hit_points <= 0:
                break
            self_hit_points -= max(1, other.damage - self_armor)
        return self_hit_points > 0


def main() -> None:
    enemy_hit_point = None
    enemy_damage = None
    enemy_armor = None
    with open(FILENAME, "r") as file:
        for line in file:
            line_split = line.strip().split(": ")
            if line_split[0] == "Hit Points":
                enemy_hit_point = int(line_split[1])
            elif line_split[0] == "Damage":
                enemy_damage = int(line_split[1])
            elif line_split[0] == "Armor":
                enemy_armor = int(line_split[1])
            else:
                raise NotImplementedError
    if enemy_hit_point is None or enemy_damage is None or enemy_armor is None:
        raise NotImplementedError
    myself = Hero(MY_HIT_POINTS, MY_DAMAGE, MY_ARMOR)
    enemy = Hero(enemy_hit_point, enemy_damage, enemy_armor)
    lowest_gold = None
    for armor in ARMOR:
        if lowest_gold is not None and ARMOR[armor][0] >= lowest_gold:
            continue
        for weapon in WEAPONS:
            if (
                lowest_gold is not None
                and ARMOR[armor][0] + WEAPONS[weapon][0] >= lowest_gold
            ):
                continue
            for ring1, ring2 in itertools.combinations(RINGS.keys(), 2):
                if (
                    lowest_gold is not None
                    and ARMOR[armor][0]
                    + WEAPONS[weapon][0]
                    + RINGS[ring1][0]
                    + RINGS[ring2][0]
                    >= lowest_gold
                ):
                    continue
                if myself.fight(
                    enemy,
                    [WEAPONS[weapon], ARMOR[armor], RINGS[ring1], RINGS[ring2]],
                ):
                    lowest_gold = (
                        ARMOR[armor][0]
                        + WEAPONS[weapon][0]
                        + RINGS[ring1][0]
                        + RINGS[ring2][0]
                    )
                    print(lowest_gold, armor, weapon, ring1, ring2)
    print(lowest_gold)


if __name__ == "__main__":
    main()
