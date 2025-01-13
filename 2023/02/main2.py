COLORS = ("red", "green", "blue")

def main():
    total_power = 0
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            gamenumber = int(line.split(":")[0].split(" ")[1])
            print(gamenumber)
            rounds = line.split(":")[1].split(";")
            max_icecubes = dict()
            for i in range(len(COLORS)):
                max_icecubes[COLORS[i]] = 0
            for round_str in rounds:
                ice_cubes = dict()
                for i in range(len(COLORS)):
                    ice_cubes[COLORS[i]] = 0
                for num, color in map(lambda x: tuple(x.strip().split(" ")),round_str.split(",")):
                    # print(num, color)
                    if color not in ice_cubes:
                        raise NotImplementedError
                    else:
                        ice_cubes[color] += int(num)
                for color in max_icecubes:
                    max_icecubes[color] = max(max_icecubes[color], ice_cubes[color])
            print(max_icecubes)
            power = 1
            for color in max_icecubes:
                if max_icecubes[color] > 0:
                    power *= max_icecubes[color]
            total_power += power
    print(total_power)

if __name__ == "__main__":
    main()
