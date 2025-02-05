FILENAME = "demo1_0.txt"  # expected 7,3
FILENAME = "demo1_1.txt"  # expected 2,2
FILENAME = "demo1_2.txt"  # expected 0,1
FILENAME = "input.txt"

CAR_SYMBOL = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
HORIZONTAL = "-"
VERTICAL = "|"
TURN_1 = "/"
TURN_2 = "\\"
CROSS = "+"
RIGHT = {
    (0, 1): [(-1, 0), (0, 1), (1, 0)],
    (1, 0): [(0, 1), (1, 0), (0, -1)],
    (0, -1): [(1, 0), (0, -1), (-1, 0)],
    (-1, 0): [(0, -1), (-1, 0), (0, 1)],
}


class Car:
    def __init__(self, y: int, x: int, dy: int, dx: int) -> None:
        self.y = y
        self.x = x
        self.dy = dy
        self.dx = dx
        self.turns = 0

    def __repr__(self) -> str:
        return f"Car({self.y,self.x} {self.dy,self.dx})"

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Car):
            raise NotImplementedError
        return self.tuple < other.tuple

    @property
    def tuple(self) -> tuple[int, int]:
        return (self.y, self.x)

    @property
    def symbol(self) -> str:
        for key, value in CAR_SYMBOL.items():
            if (self.dy, self.dx) == value:
                return key
        raise NotImplementedError

    def next_turn(self) -> None:
        self.dy, self.dx = RIGHT[self.dy, self.dx][self.turns % (len(RIGHT[self.dy, self.dx]))]
        self.turns += 1


def show_map(the_map: list[str], cars: set[Car]) -> None:
    cars_tuple = {x.tuple: x.symbol for x in cars}
    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            if (y, x) in cars_tuple:
                symbol = cars_tuple[y, x]
            else:
                symbol = the_map[y][x]
            print(symbol, end="")
        print()


def main() -> None:
    the_map: list[str] = []
    cars: set[Car] = set()
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_ if line_[-1] != "\n" else line_[:-1]
            for car_symbol in CAR_SYMBOL:
                while car_symbol in line:
                    car_index = line.index(car_symbol)
                    cars.add(
                        Car(
                            len(the_map),
                            car_index,
                            CAR_SYMBOL[car_symbol][0],
                            CAR_SYMBOL[car_symbol][1],
                        )
                    )
                    if CAR_SYMBOL[car_symbol][1] == 0:
                        car_replace = VERTICAL
                    elif CAR_SYMBOL[car_symbol][0] == 0:
                        car_replace = HORIZONTAL
                    else:
                        print(f"line = {line}")
                        raise NotImplementedError
                    line = line[:car_index] + car_replace + line[car_index + 1 :]
            print(line)
            the_map.append(line)
    print(cars)
    show_map(the_map, cars)
    car_positions: set[tuple[int, int]] = set(map(lambda x: x.tuple, cars))
    while True:
        for car in sorted(cars):
            car_positions.remove(car.tuple)
            car.y += car.dy
            car.x += car.dx
            if car.tuple in car_positions:
                print(f"{car.x},{car.y}")
                return
            car_positions.add(car.tuple)
            if car.dy == 0 and the_map[car.y][car.x] == HORIZONTAL:
                pass
            elif car.dx == 0 and the_map[car.y][car.x] == VERTICAL:
                pass
            elif the_map[car.y][car.x] == CROSS:
                car.next_turn()
            elif the_map[car.y][car.x] == TURN_1:
                if car.dy == 0 and car.dx == 1:
                    car.dy = -1
                    car.dx = 0
                elif car.dy == -1 and car.dx == 0:
                    car.dy = 0
                    car.dx = 1
                elif car.dy == 0 and car.dx == -1:
                    car.dy = 1
                    car.dx = 0
                elif car.dy == 1 and car.dx == 0:
                    car.dy = 0
                    car.dx = -1
                else:
                    print(
                        f"car.dy = {car.dy} car.dx = {car.dx} the_map[{car.y}][{car.x}] = {the_map[car.y][car.x]}"
                    )
                    raise NotImplementedError
            elif the_map[car.y][car.x] == TURN_2:
                if car.dy == 0 and car.dx == 1:
                    car.dy = 1
                    car.dx = 0
                elif car.dy == -1 and car.dx == 0:
                    car.dy = 0
                    car.dx = -1
                elif car.dy == 1 and car.dx == 0:
                    car.dy = 0
                    car.dx = 1
                elif car.dy == 0 and car.dx == -1:
                    car.dy = -1
                    car.dx = 0
                else:
                    print(
                        f"car.dy = {car.dy} car.dx = {car.dx} the_map[{car.y}][{car.x}] = {the_map[car.y][car.x]}"
                    )
                    raise NotImplementedError
            else:
                print(
                    f"car.dy = {car.dy} car.dx = {car.dx} the_map[{car.y}][{car.x}] = {the_map[car.y][car.x]}"
                )
                raise NotImplementedError
        # print(cars)
        # show_map(the_map, cars)


if __name__ == "__main__":
    main()
