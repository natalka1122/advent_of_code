from __future__ import annotations
from typing import Optional, TextIO

FILENAME="input.txt"
#FILENAME = "demo.txt"


class Segment:
    def __init__(
        self, start: int, end: Optional[int] = None, range: Optional[int] = None
    ) -> None:
        self.start = start
        if end is None:
            if range is None:
                raise NotImplementedError
            self.range = range
            self.end = start + range
        elif range is None:
            if end is None:
                raise NotImplementedError
            self.end = end
            self.range = end - start
        else:
            raise NotImplementedError
        if self.range <= 0:
            print(
                f"self.start = {self.start} self.end = {self.end} self.range = {self.range}"
            )
            raise NotImplementedError
        if self.start < 0:
            print(
                f"self.start = {self.start} self.end = {self.end} self.range = {self.range}"
            )
            raise NotImplementedError

    def __repr__(self) -> str:
        return f"[{self.start}, {self.end})"

    def __lt__(self, other: Segment) -> bool:
        return self.start < other.start

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Segment)
            and self.start == other.start
            and self.end == other.end
            and self.range == other.range
        )

    def __hash__(self) -> int:
        return hash((self.start, self.end))

    def meet(self, other: Segment) -> tuple[list[Segment], list[Segment]]:
        # First list of Segments is covered by map, second is list of Segments not covered my map
        # print(f"self = {self} other = {other}")
        if self.start < other.start:
            if self.end <= other.start:
                # print(f"self = {self} other = {other}")
                return ([], [self])
            elif other.start < self.end <= other.end:
                # print(f"self = {self} other = {other}")
                return (
                    [Segment(start=other.start, end=self.end)],
                    [Segment(start=self.start, end=other.start)],
                )
            elif other.end < self.end:
                # print(f"self = {self} other = {other}")
                return (
                    [Segment(start=other.start, end=other.end)],
                    [
                        Segment(start=self.start, end=other.start),
                        Segment(start=other.end, end=self.end),
                    ],
                )
        elif other.start <= self.start < other.end:
            if self.end <= other.end:
                # print(f"self = {self} other = {other}")
                return ([self], [])
            elif other.end < self.end:
                # print(f"self = {self} other = {other}")
                return (
                    [Segment(start=self.start, end=other.end)],
                    [Segment(start=other.end, end=self.end)],
                )
            else:
                print(f"self = {self} other = {other}")
                raise NotImplementedError
        elif other.end <= self.start:
            # print(f"self = {self} other = {other}")
            return ([], [self])
        else:
            print(f"self = {self} other = {other}")
            raise NotImplementedError
        raise NotImplementedError


def read_expected_line(file: TextIO, expected: str) -> None:
    line = file.readline().strip()
    if line != expected:
        print(f"line = {line} expected = {expected}")
        raise NotImplementedError


def from_source_to_destination(
    source_segments: list[Segment], the_map: set[tuple[int, Segment]]
) -> list[Segment]:
    # print(f"source_segments = {source_segments} the_map = {the_map}")
    result: list[Segment] = list()
    i = 0
    while i < len(source_segments):
        source_segment = source_segments[i]
        found_map_segment = False
        for dst, map_segment in the_map:
            inside_of_map, outside_of_map = source_segment.meet(map_segment)
            if len(inside_of_map) > 0:
                found_map_segment = True
                for segment in inside_of_map:
                    result.append(
                        Segment(
                            start=dst + segment.start - map_segment.start,
                            range=segment.range,
                        )
                    )
                source_segments.extend(outside_of_map)
                break
        if not found_map_segment:
            result.append(source_segment)
        i += 1

    return result


def read_and_transpose(
    file: TextIO, expected_str: str, source_segments: list[Segment]
) -> list[Segment]:
    read_expected_line(file, expected_str)
    the_map: set[tuple[int, Segment]] = set()
    while True:
        line = file.readline().strip()
        if len(line) == 0:
            break
        line_split = line.split(" ")
        if len(line_split) != 3:
            raise NotImplementedError
        the_map.add(
            (
                int(line_split[0]),
                Segment(start=int(line_split[1]), range=int(line_split[2])),
            )
        )
    return from_source_to_destination(source_segments, the_map)


def main() -> None:
    with open(FILENAME, "r") as file:
        seed_list: list[int] = list(
            map(int, file.readline().split(":")[1].strip().split(" "))
        )
        seed_segments: list[Segment] = list(
            Segment(start=seed_list[i], range=seed_list[i + 1])
            for i in range(0, len(seed_list), 2)
        )
        print(f"seed_segments = {seed_segments}")
        read_expected_line(file, "")
        soil_segments = read_and_transpose(file, "seed-to-soil map:", seed_segments)
        print(f"soil_segments = {soil_segments}")
        print("1/7", len(soil_segments), "=" * 20)
        fertilizer_segments = read_and_transpose(
            file, "soil-to-fertilizer map:", soil_segments
        )
        print(f"fertilizer_segments = {fertilizer_segments}")
        print("2/7", len(fertilizer_segments), "=" * 20)
        water_segments = read_and_transpose(
            file, "fertilizer-to-water map:", fertilizer_segments
        )
        print(f"water_segments = {water_segments}")
        print("3/7", len(water_segments), "=" * 20)
        light_segments = read_and_transpose(file, "water-to-light map:", water_segments)
        print(f"light_segments = {light_segments}")
        print("4/7", len(light_segments), "=" * 20)
        temperature_segments = read_and_transpose(
            file, "light-to-temperature map:", light_segments
        )
        print(f"temperature_segments = {temperature_segments}")
        print("5/7", len(temperature_segments), "=" * 20)
        humidity_segments = read_and_transpose(
            file, "temperature-to-humidity map:", temperature_segments
        )
        print(f"humidity_segments = {humidity_segments}")
        print("6/7", len(humidity_segments), "=" * 20)
        location_segments = read_and_transpose(
            file, "humidity-to-location map:", humidity_segments
        )
        print(f"location_segments = {location_segments}")
        print("7/7", len(location_segments), "=" * 20)
    print(min(location_segments))


if __name__ == "__main__":
    main()
