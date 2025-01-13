NUMBERS = "1234567890"
EXCLUDE_SYMBOL = "."
ENGINE_CENTER = "*"

def calc_gear(engine,y,x):
    print(f"candidate {y} {x}")
    neighbors = set()
    for y0 in range(max(0, y-1), min(len(engine), y+2)):
        for x0 in range(max(0, x-1), min(len(engine[y]), x+2)):
            if engine[y0][x0] in NUMBERS:
                # print(f"neighbor candidate {y0} {x0}")
                x1 = x0
                while x1 > 0 and engine[y0][x1-1] in NUMBERS:
                    x1 -= 1
                # print(f"neighbor candidate y0={y0} x0={x0} x1={x1}")
                x2 = x0
                while x2 < len(engine[y])-1 and engine[y0][x2+1] in NUMBERS:
                    x2 += 1
                print(f"neighbor candidate y0={y0} x0={x0} x1={x1} x2={x2} value={engine[y0][x1:x2+1]}")
                neighbors.add((int(engine[y0][x1:x2+1]), y0,x1,x2))
    print(neighbors)
    if len(neighbors) != 2:
        return 0
    result = 1
    for neighbor in neighbors:
      result *= neighbor[0]
    return result

def main():
    engine = []
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            engine.append(line.strip())
    engine_sum = 0
    for y in range(len(engine)):
        for x in range(len(engine[y])):
            if engine[y][x] == ENGINE_CENTER:
                engine_sum += calc_gear(engine,y,x)

    print(engine_sum)

if __name__ == "__main__":
    main()