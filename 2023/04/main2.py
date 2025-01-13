def main():
    cards = dict()
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            card_number = int(list(filter(None, line.split(":")[0].split(" ")))[1])
            winning_cards = set(map(int,filter(None,line.split(":")[1].split("|")[0].strip().split(" "))))
            i_have_cards = set(map(int,filter(None, line.split("|")[1].strip().split(" "))))
            # print(winning_cards, i_have_cards)
            score = 0
            for card in i_have_cards:
                if card in winning_cards:
                    score += 1
            print(f"score = {score}")
            cards[card_number] = [score, 1]
    print(cards)
    total_cards = 0
    for card_number in sorted(cards):
        print(card_number, cards[card_number], list(range(card_number, card_number+cards[card_number][0]+1)))
        for i in range(card_number+1, card_number+cards[card_number][0]+1):
            # print(f"i = {i}")
            if i in cards:
                cards[i][1] += cards[card_number][1]
        total_cards += cards[card_number][1]
    print(cards)
    print(total_cards)

if __name__ == "__main__":
    main()