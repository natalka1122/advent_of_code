# type: ignore
import matplotlib.pyplot as plt

border = [
    (2, 3),
    (2, 4),
    (2, 5),
    (3, 3),
    (3, 5),
    (6, 3),
    (6, 5),
    (7, 1),
    (7, 2),
    (7, 3),
    (7, 5),
    (8, 1),
    (8, 5),
    (9, 1),
    (9, 5),
    (9, 6),
    (9, 7),
    (10, 1),
    (10, 7),
    (11, 1),
    (11, 2),
    (11, 3),
    (11, 4),
    (11, 5),
    (11, 6),
    (11, 7),
]
outside = [
    (1, 0),
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (2, 0),
    (2, 1),
    (2, 2),
    (2, 6),
    (2, 7),
    (2, 8),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 6),
    (3, 7),
    (3, 8),
    (6, 0),
    (6, 1),
    (6, 2),
    (6, 6),
    (6, 7),
    (6, 8),
    (7, 0),
    (7, 6),
    (7, 7),
    (7, 8),
    (8, 0),
    (8, 6),
    (8, 7),
    (8, 8),
    (9, 0),
    (9, 8),
    (10, 0),
    (10, 8),
    (11, 0),
    (11, 8),
    (12, 0),
    (12, 1),
    (12, 2),
    (12, 3),
    (12, 4),
    (12, 5),
    (12, 6),
    (12, 7),
    (12, 8),
]

x_border, y_border = zip(*border)
x_outside, y_outside = zip(*outside)

plt.figure(figsize=(6, 6))
plt.scatter(x_border, y_border, color="red")
plt.scatter(x_outside, y_outside, color="black")
plt.gca().set_aspect("equal", adjustable="box")

plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
