import random
import matplotlib.pyplot as plt
def plot(points):
    xx = [x for (x, y) in points]
    yy = [y for (x, y) in points]
    plt.plot(xx, yy, 'g.')
    plt.show()
def sierpinski(n):
    vertices = [(0.0, 0.0), (0.5, 1.0), (1.0, 0.0)]
    points = []
    x, y = random.choice(vertices)
    for i in range(n):
        vx, vy = random.choice(vertices)
        x = (vx + x) / 2.0
        y = (vy + y) / 2.0
        points.append((x, y))
    plot(points)
sierpinski(n=999999)
