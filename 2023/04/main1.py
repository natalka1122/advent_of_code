def main():
    result = 0
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            winning_cards = set(map(int,filter(None,line.split(":")[1].split("|")[0].strip().split(" "))))
            i_have_cards = set(map(int,filter(None, line.split("|")[1].strip().split(" "))))
            print(winning_cards, i_have_cards)
            score = 0
            for card in i_have_cards:
                if card in winning_cards:
                    score += 1
            print(f"score = {score}")
            if score > 0:
                result += 2**(score-1)
    print(result)

if __name__ == "__main__":
    main()