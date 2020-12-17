from voronoi import Point, Triangle, Voronoi
import matplotlib.pyplot as plt
import numpy as np

t = Triangle(Point(0,0), Point(3,0), Point(1,4))
t1 = Triangle(Point(10,2), Point(3,0), Point(1,4))
p1 = Point(1.5, 2)
p2 = Point(10, 4)

# print(t.cradius)
# print(t.ccenter)

# print("in triag t")
# print(p1.inTriagCercumC(t))
# print(p2.inTriagCercumC(t))
# print("in triag T1")
# print(p1.inTriagCercumC(t1))
# print(p2.inTriagCercumC(t1))



# points = np.random.randint(100, 200, size=(100, 2))
# points = np.array([[0,0], [10,0], [10,10], [0,10]])
# print(points)
points = [[p1, p2] for p1 in range(10) for p2 in range(10)]

vor = Voronoi(points)
# print(vor.points)
vor.draw()

# plt.figure()
# plt.grid(True, which='both')
# t.draw()
# t1.draw()
# plt.axhline(y=0, color='k')
# p1.draw()
# p2.draw()
# plt.axvline(x=0, color='k')
# plt.show()
