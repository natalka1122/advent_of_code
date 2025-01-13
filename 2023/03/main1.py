NUMBERS = "1234567890"
EXCLUDE_SYMBOL = "."

def find_number(engine):
    for y in range(len(engine)):
        x = 0
        while x < len(engine[y]):
            if engine[y][x] in NUMBERS:
                x1 = x
                x2 = x+1
                while x2 < len(engine[y]) and engine[y][x2] in NUMBERS:
                    x2 += 1
                    x+= 1
                yield int(engine[y][x1:x2]), y, x1, x2
            x+=1

def check_symbols(engine, number, y, x1,x2):
    for i in range(max(0, y-1), min(len(engine), y+2)):
        for j in range(max(0, x1-1), min(len(engine[y]), x2+1)):
            if engine[i][j] not in NUMBERS and engine[i][j] not in EXCLUDE_SYMBOL:
                print(number,i,j,engine[i][j], "!!!")
                return True
    print(number, "NOPE")
    return False

def main():
    engine = []
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            engine.append(line.strip())
    engine_sum = 0
    for number, y,x1,x2 in find_number(engine):
        print(f"number = {number} y = {y} x1 = {x1} x2 = {x2}")
        if check_symbols(engine, number, y, x1,x2):
            engine_sum += number
    # for y in range(len(engine)):
    #     x = 0
    #     while x < len(engine[y]):
    #     for x in range(len(engine[y])):
    #         if engine[y][x] in NUMBERS:
    #             add_me = False
    #             for y1 in range(max(0, y-1), min(len(engine), y+1)):
    #                 for x1 in range(max(0, x-1), min(len(engine[y]), x+1)):
    #                     print(f"y1 = {y1} x1 = {x1}")
    #                     if engine[y1][x1] not in NUMBERS and engine[y1][x1] not in EXCLUDE_SYMBOL:
    #                         add_me = True
    #                         break
    #                 if add_me:
    #                     break
    #             if add_me:
    #                 engine_sum += int(engine[y][x])
    print(engine_sum)

if __name__ == "__main__":
    main()