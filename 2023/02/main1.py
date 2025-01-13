COLORS = ("red", "green", "blue")
CUBES = (12, 13, 14)

def main():
    impossibles = 0
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            impossible = False
            gamenumber = int(line.split(":")[0].split(" ")[1])
            print(gamenumber)
            rounds = line.split(":")[1].split(";")
            for round_str in rounds:
                ice_cubes = dict()
                for i in range(len(COLORS)):
                    ice_cubes[COLORS[i]] = CUBES[i]
                for num, color in map(lambda x: tuple(x.strip().split(" ")),round_str.split(",")):
                    print(num, color)
                    if color not in ice_cubes:
                        raise NotImplementedError
                    else:
                        ice_cubes[color] -= int(num)
                    if ice_cubes[color] < 0:
                        impossible = True
                        
                print(impossible, ice_cubes)
                # print(list(map(lambda x: tuple(x.strip().split(" ")),round_str.split(","))))
            if not impossible:
                impossibles += gamenumber
                print("!!!", gamenumber)
    print(impossibles)

if __name__ == "__main__":
    main()
