from __future__ import annotations
from typing import Iterator

FILENAME, MY_HIT_POINTS, MY_MANA = "input.txt", 50, 500
FIRST_DEAD = -1
SECOND_DEAD = 1
BOTH_ALIVE = 0
BOTH_DEAD = 2


class Spell:
    def __init__(
        self,
        price: int = 0,
        damage: int = 0,
        heal: int = 0,
        lasts_for: int = 0,
        add_armor: int = 0,
        add_damage: int = 0,
        add_mana: int = 0,
    ):
        self.price = price
        self.damage = damage
        self.heal = heal
        self.lasts_for = lasts_for
        self.add_armor = add_armor
        self.add_damage = add_damage
        self.add_mana = add_mana

    def __repr__(self) -> str:
        result = dict()
        for key, value in self.__dict__.items():
            if value > 0:
                result[key] = value
        return str(result)


SHIELD = "Shield"
POISON = "Poison"
RECHARGE = "Recharge"
SPELLS = {
    "Magic Missile": Spell(price=53, damage=4),
    "Drain": Spell(price=73, damage=2, heal=2),
    SHIELD: Spell(price=113, lasts_for=6, add_armor=7),
    POISON: Spell(price=173, lasts_for=6, add_damage=3),
    RECHARGE: Spell(price=229, lasts_for=5, add_mana=101),
}


class Hero:
    def __init__(
        self,
        hit_points: int,
        mana: int = 0,
        attack: int = 0,
        armor: int = 0,
        shield_left: int = 0,
        poison_left: int = 0,
        recharge_left: int = 0,
    ) -> None:
        if mana != 0 and attack != 0:
            raise NotImplementedError
        if any(
            map(
                lambda x: x < 0,
                [
                    hit_points,
                    mana,
                    attack,
                    armor,
                    shield_left,
                    poison_left,
                    recharge_left,
                ],
            )
        ):
            raise NotImplementedError
        self.hit_points = hit_points
        self.mana = mana
        self.attack = attack
        self.armor = armor
        self.shield_left = shield_left
        self.poison_left = poison_left
        self.recharge_left = recharge_left

    def __repr__(self) -> str:
        result = dict()
        for key, value in self.__dict__.items():
            if key == "hit_points" or value > 0:
                result[key] = value
        return str(result)

    def is_alive(self) -> bool:
        return self.hit_points > 0

    def get_possible_spells(self) -> Iterator[Spell]:
        if self.mana == 0 and self.attack > 0:
            yield Spell(damage=self.attack)
        elif self.mana > 0 and self.attack == 0:
            for spell in SPELLS.values():
                if spell.price <= self.mana:
                    if spell.add_armor > 0:
                        if self.shield_left <= 1:
                            yield spell
                    elif spell.add_damage > 0:
                        if self.poison_left <= 1:
                            yield spell
                    elif spell.add_mana > 0:
                        if self.recharge_left <= 1:
                            yield spell
                    else:
                        yield spell
        else:
            raise NotImplementedError

    def do_spell(self, other: Hero, spell: Spell) -> tuple[int, Hero, Hero]:
        if spell.price > self.mana:
            print(f"{self} cannot afford {spell}")
            raise NotImplementedError
        new_self = Hero(
            hit_points=self.hit_points,
            mana=self.mana - spell.price,
            attack=self.attack,
            armor=self.armor,
            shield_left=self.shield_left,
            poison_left=self.poison_left,
            recharge_left=self.recharge_left,
        )
        new_other = Hero(
            hit_points=other.hit_points,
            mana=other.mana,
            attack=other.attack,
            armor=other.armor,
            shield_left=other.shield_left,
            poison_left=other.poison_left,
            recharge_left=other.recharge_left,
        )
        # Check vitals
        new_self_is_alive = new_self.is_alive()
        new_other_is_alive = new_other.is_alive()
        if new_self_is_alive and not new_other_is_alive:
            return SECOND_DEAD, new_self, new_other
        if not new_self_is_alive and new_other_is_alive:
            return FIRST_DEAD, new_self, new_other
        if not new_self_is_alive and not new_other_is_alive:
            return BOTH_DEAD, new_self, new_other        
        # Apply previous spells
        if self.shield_left > 0:
            new_self.armor = SPELLS[SHIELD].add_armor
            new_self.shield_left -= 1
        else:
            new_self.armor = 0
        if self.poison_left > 0:
            new_other.hit_points -= SPELLS[POISON].add_damage
            new_self.poison_left -= 1
        if self.recharge_left > 0:
            new_self.mana += SPELLS[RECHARGE].add_mana
            new_self.recharge_left -= 1
        if other.shield_left > 0:
            new_other.armor = SPELLS[SHIELD].add_armor
            new_other.shield_left -= 1
        else:
            new_other.armor = 0
        if other.poison_left > 0:
            new_self.hit_points -= SPELLS[POISON].add_damage
            new_other.poison_left -= 1
        if other.recharge_left > 0:
            new_other.mana += SPELLS[RECHARGE].add_mana
            new_other.recharge_left -= 1
        # Check vitals
        new_self_is_alive = new_self.is_alive()
        new_other_is_alive = new_other.is_alive()
        if new_self_is_alive and not new_other_is_alive:
            return SECOND_DEAD, new_self, new_other
        if not new_self_is_alive and new_other_is_alive:
            return FIRST_DEAD, new_self, new_other
        if not new_self_is_alive and not new_other_is_alive:
            return BOTH_DEAD, new_self, new_other
        # Apply current spell
        if spell.add_armor > 0:
            if new_self.shield_left > 0:
                raise NotImplementedError
            new_self.shield_left = spell.lasts_for
        elif spell.add_damage > 0:
            if new_self.poison_left > 0:
                raise NotImplementedError
            new_self.poison_left = spell.lasts_for
        elif spell.add_mana > 0:
            if new_self.recharge_left > 0:
                raise NotImplementedError
            new_self.recharge_left = spell.lasts_for
        else:
            new_other.hit_points -= max(1, spell.damage - new_other.armor)
            new_self.hit_points += spell.heal
        new_self_is_alive = new_self.is_alive()
        new_other_is_alive = new_other.is_alive()
        if new_self_is_alive and new_other_is_alive:
            return BOTH_ALIVE, new_self, new_other
        if new_self_is_alive and not new_other_is_alive:
            return SECOND_DEAD, new_self, new_other
        if not new_self_is_alive and new_other_is_alive:
            return FIRST_DEAD, new_self, new_other
        if not new_self_is_alive and not new_other_is_alive:
            return BOTH_DEAD, new_self, new_other
        raise NotImplementedError


def main() -> None:
    enemy_hit_point = None
    enemy_damage = None
    with open(FILENAME, "r") as file:
        for line in file:
            line_split = line.strip().split(": ")
            if line_split[0] == "Hit Points":
                enemy_hit_point = int(line_split[1])
            elif line_split[0] == "Damage":
                enemy_damage = int(line_split[1])
            else:
                raise NotImplementedError
    if enemy_hit_point is None or enemy_damage is None:
        raise NotImplementedError
    myself = Hero(MY_HIT_POINTS, mana=MY_MANA)
    enemy = Hero(enemy_hit_point, attack=enemy_damage)
    paths = {(0, True, myself, enemy)}
    best_result = None
    while len(paths) > 0:
        cost, is_my_turn, myself, enemy = paths.pop()
        # print()
        # print(
        #     f"cost = {cost} is_my_turn = {is_my_turn} myself = {myself} enemy = {enemy}"
        # )
        if best_result is not None and cost > best_result:
            continue
        if is_my_turn:
            myself.hit_points -=1
            for spell in myself.get_possible_spells():
                current, new_myself, new_enemy = myself.do_spell(enemy, spell)
                if current == FIRST_DEAD or current == BOTH_DEAD:
                    # print(
                    #     f"{spell} FIRST_DEAD or BOTH_DEAD: {current} {new_myself} {new_enemy}"
                    # )
                    pass
                elif current == SECOND_DEAD:
                    if best_result is None or spell.price + cost < best_result:
                        best_result = spell.price + cost
                    # print(f"{spell} SECOND_DEAD {new_myself} {new_enemy}")
                elif current == BOTH_ALIVE:
                    paths.add((spell.price + cost, False, new_myself, new_enemy))
                    # print(f"{spell} BOTH_ALIVE {new_myself} {new_enemy}")
                else:
                    raise NotImplementedError
        else:
            for spell in enemy.get_possible_spells():
                current, new_enemy, new_myself = enemy.do_spell(myself, spell)
                if current == SECOND_DEAD or current == BOTH_DEAD:
                    # print(
                    #     f"{spell} SECOND_DEAD or BOTH_DEAD: {current}  {new_myself} {new_enemy}"
                    # )
                    pass
                elif current == FIRST_DEAD:
                    if best_result is None or spell.price + cost < best_result:
                        best_result = spell.price + cost
                    # print(f"{spell} FIRST_DEAD {new_myself} {new_enemy}")
                elif current == BOTH_ALIVE:
                    paths.add((spell.price + cost, True, new_myself, new_enemy))
                    # print(f"{spell} BOTH_ALIVE {new_myself} {new_enemy}")
                else:
                    raise NotImplementedError
    print(best_result)


if __name__ == "__main__":
    main()
