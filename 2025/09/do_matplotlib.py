# type: ignore
import matplotlib.pyplot as plt 

border = [
    (2, 3),
    (2, 3.5),
    (2, 4.5),
    (2, 5),
    (2.5, 3),
    (2.5, 5),
    (6.5, 3),
    (6.5, 5),
    (7, 1),
    (7, 1.5),
    (7, 2.5),
    (7, 3),
    (7, 5),
    (7.5, 1),
    (7.5, 5),
    (8.5, 1),
    (8.5, 5),
    (9, 1),
    (9, 5),
    (9, 5.5),
    (9, 6.5),
    (9, 7),
    (9.5, 1),
    (9.5, 7),
    (10.5, 1),
    (10.5, 7),
    (11, 1),
    (11, 1.5),
    (11, 2.5),
    (11, 3),
    (11, 3.5),
    (11, 4.5),
    (11, 5),
    (11, 5.5),
    (11, 6.5),
    (11, 7),
]
x0, y0 = zip(*border)

plt.figure(figsize=(6, 6))
plt.scatter(x0, y0, color="black")
plt.gca().set_aspect("equal", adjustable="box")

plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
