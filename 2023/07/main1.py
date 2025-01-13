from __future__ import annotations
from collections import Counter

# FILENAME = "demo1.txt"
# FILENAME = "demo2.txt"
# FILENAME = "demo3.txt"
# FILENAME = "demo4.txt"
# FILENAME = "demo.txt"
FILENAME = "input.txt"
CARDS = "23456789TJQKA"
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


class Hand:
    def __init__(self, hand_str: str, bid: int):
        if len(hand_str) != 5:
            print(f"hand_str = {len(hand_str)} {hand_str}")
            raise NotImplementedError
        self.bid = bid
        self._cards = list(map(Card, hand_str))
        self._str = "".join(map(str, self._cards))
        values = sorted(Counter(self._str).values())
        if values == [5]:
            self._type = FIVE_OF_A_KIND
            return
        if values == [1, 4]:
            self._type = FOUR_OF_A_KIND
            return
        if values == [2, 3]:
            self._type = FULL_HOUSE
            return
        if values == [1, 1, 3]:
            self._type = THREE_OF_A_KIND
            return
        if values == [1, 2, 2]:
            self._type = TWO_PAIR
            return
        if values == [1, 1, 1, 2]:
            self._type = ONE_PAIR
            return
        if values == [1, 1, 1, 1, 1]:
            self._type = HIGH_CARD
            return
        print(f"values = {values}")
        raise NotImplementedError

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
