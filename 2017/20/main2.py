from __future__ import annotations
import re

FILENAME = "demo2.txt"  # expected 1
FILENAME = "input.txt"

# I am lazy today
BIG_NUMBER_OF_STEPS = 5000


class Particle:
    def __init__(
        self, x: int, y: int, z: int, dx: int, dy: int, dz: int, ax: int, ay: int, az: int
    ):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.ax = ax
        self.ay = ay
        self.az = az

    def get_next(self) -> None:
        self.dx += self.ax
        self.dy += self.ay
        self.dz += self.az
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    def tuple(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)


def main() -> None:
    particles: list[Particle] = []
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"p=< ?(-?\d+),(-?\d+),(-?\d+)>, v=< ?(-?\d+),(-?\d+),(-?\d+)>, a=< ?(-?\d+),(-?\d+),(-?\d+)>",
                line,
            )
            if line_match is None:
                raise NotImplementedError
            particles.append(Particle(*map(int, line_match.groups())))
    for t in range(BIG_NUMBER_OF_STEPS):
        current_pos: dict[tuple[int, int, int], Particle] = dict()
        anihilate = set()
        for particle in particles:
            particle.get_next()
            particle_tuple = particle.tuple()
            if particle_tuple in current_pos:
                anihilate.add(current_pos[particle_tuple])
                anihilate.add(particle)
            else:
                current_pos[particle_tuple] = particle
        if len(anihilate) > 0:
            print(t, anihilate)
        for particle in anihilate:
            particles.remove(particle)
    print(len(particles))


if __name__ == "__main__":
    main()
