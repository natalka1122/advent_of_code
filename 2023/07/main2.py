from __future__ import annotations
from collections import Counter

# FILENAME = "demo1.txt"
# FILENAME = "demo2.txt"
# FILENAME = "demo3.txt"
# FILENAME = "demo4.txt"
# FILENAME = "demo.txt"
FILENAME = "input.txt"
CARDS = "J23456789TQKA"
J = "J"
FIVE_OF_A_KIND = 1
FOUR_OF_A_KIND = 2
FULL_HOUSE = 3
THREE_OF_A_KIND = 4
TWO_PAIR = 5
ONE_PAIR = 6
HIGH_CARD = 7


class Card:
    def __init__(self, card_str: str):
        if card_str not in CARDS:
            print(f"card_str = {card_str}")
            raise NotImplementedError
        self._strength = CARDS.index(card_str)
        self._card = card_str

    def __str__(self) -> str:
        return self._card

    def __lt__(self, other: Card) -> bool:
        return self._strength < other._strength


def get_card_type(j_count: int, values: list[int]) -> int:
    if j_count == 5:
        return FIVE_OF_A_KIND
    if j_count == 4:
        return FIVE_OF_A_KIND
    if j_count == 3:
        if values == [1, 1]:
            return FOUR_OF_A_KIND
        if values == [2]:
            return FIVE_OF_A_KIND
    if j_count == 2:
        if values == [1, 1, 1]:
            return THREE_OF_A_KIND
        if values == [1, 2]:
            return FOUR_OF_A_KIND
        if values == [3]:
            return FIVE_OF_A_KIND
    if j_count == 1:
        if values == [1, 1, 1, 1]:
            return ONE_PAIR
        if values == [1, 1, 2]:
            return THREE_OF_A_KIND
        if values == [2, 2]:
            return FULL_HOUSE
        if values == [1, 3]:
            return FOUR_OF_A_KIND
        if values == [4]:
            return FIVE_OF_A_KIND
    if j_count == 0:
        if values == [5]:
            return FIVE_OF_A_KIND
        if values == [1, 4]:
            return FOUR_OF_A_KIND
        if values == [2, 3]:
            return FULL_HOUSE
        if values == [1, 1, 3]:
            return THREE_OF_A_KIND
        if values == [1, 2, 2]:
            return TWO_PAIR
        if values == [1, 1, 1, 2]:
            return ONE_PAIR
        if values == [1, 1, 1, 1, 1]:
            return HIGH_CARD
    print(f"j_count = {j_count} values = {values}")
    raise NotImplementedError


class Hand:
    def __init__(self, hand_str: str, bid: int):
        if len(hand_str) != 5:
            print(f"hand_str = {len(hand_str)} {hand_str}")
            raise NotImplementedError
        self.bid = bid
        self._cards = list(map(Card, hand_str))
        self._str = "".join(map(str, self._cards))
        self._type = get_card_type(
            self._str.count(J), sorted(Counter(self._str.replace(J, "")).values())
        )

    def __str__(self):
        return f"{self._type}_{self._str}"

    def __repr__(self):
        return str(self)

    def __lt__(self, other: Hand) -> bool:
        if self._type > other._type:
            return True
        if self._type < other._type:
            return False
        for index in range(len(self._str)):
            if self._cards[index] < other._cards[index]:
                return True
            if self._cards[index] > other._cards[index]:
                return False
        return False


def main():
    result = 0
    hands = []
    with open(FILENAME, "r") as file:
        for line in file:
            hand_str, bid = line.split(" ")
            hands.append(Hand(hand_str, int(bid)))
    hands = sorted(hands)
    print(hands)
    result = 0
    for index, hand in enumerate(hands):
        result += hand.bid * (index + 1)
        # print(hand.bid, index + 1)
    print(result)


if __name__ == "__main__":
    main()
