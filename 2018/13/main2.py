FILENAME = "demo2.txt"  # expected 6,4
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
        self.is_dead = False

    def __repr__(self) -> str:
        if self.is_dead:
            return "RIP"
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
    cars_tuple = {x.tuple: x for x in cars}
    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            if (y, x) in cars_tuple and not cars_tuple[y, x].is_dead:
                symbol = cars_tuple[y, x].symbol
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
            the_map.append(line)
    # print(cars)
    # show_map(the_map, cars)
    car_positions: dict[tuple[int, int], Car] = {car.tuple: car for car in cars}
    cars_alive = len(cars)
    while cars_alive > 1:
        for car in sorted(cars):
            if car.is_dead:
                continue
            car_tuple = car.tuple
            if car_tuple not in car_positions:
                raise NotImplementedError
            del car_positions[car_tuple]
            car.y += car.dy
            car.x += car.dx
            if car.tuple in car_positions:
                print(f"{car.x},{car.y} crash")
                car.is_dead = True
                car_positions[car.y, car.x].is_dead = True
                del car_positions[car.y, car.x]
                cars_alive -= 2
                continue
            car_positions[car.tuple] = car
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
    for car in cars:
        if not car.is_dead:
            print(f"{car.x},{car.y}")


if __name__ == "__main__":
    main()
