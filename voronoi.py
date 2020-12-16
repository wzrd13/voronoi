from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x == other.x
                    and self.y == other.y
                    # and self.z == other.z
            )
        return False

    # def __sub__(self, other):
        # return (self.x - other.x, self.y - other.y, self.z - other.z)

    # def __repr__(self):
    #     return repr((self.x, self.y, self.z))

    def __hash__(self):
        return hash((self.x, self.y))

    def inTriagCercumC(self, t):
        cx, cy = t.ccenter[0:2]
        return (self.x - cx)**2 + (self.y - cy)**2 < t.cradius**2
        # m1 = np.asarray([p.getCoords() - self.getCoords() for p in t.getPoints()])
        # m2 = np.sum(np.square(m1), axis=1).reshape((3, 1))
        # m = np.hstack((m1, m2))    # The 3x3 matrix to check
        # return np.linalg.det(m) <= 0

    def getCoords(self):
        return np.array([self.x, self.y])

    def draw(self):
        plt.plot(self.x, self.y, marker='o', markersize=3, color='red')


class Triangle:
    def __init__(self, a_point, b_point, c_point):
        self.a = a_point
        self.b = b_point
        self.c = c_point
        self.cradius, self.ccenter = self.cercumc()

    def cercumc(self):
        # 2D implemetation
        d = 2*(self.a.x*(self.b.y-self.c.y)
                + self.b.x*(self.c.y-self.a.y)
                + self.c.x*(self.a.y-self.b.y))

        axy = self.a.x**2 + self.a.y**2
        bxy = self.b.x**2 + self.b.y**2
        cxy = self.c.x**2 + self.c.y**2

        centerx = (axy*(self.b.y - self.c.y)
        + bxy*(self.c.y - self.a.y)
        + cxy*(self.a.y - self.b.y))/d

        centery = (axy*(self.c.x - self.b.x)
        + bxy*(self.a.x - self.c.x)
        + cxy*(self.b.x - self.a.x))/d

        cradius = sqrt((centerx-self.a.x)**2 + (centery-self.a.y)**2)
        ccenter = (centerx, centery)

        # a = np.array(self.a - self.c)
        # b = np.array(self.b - self.c)
        # ap2 = np.inner(a,a)
        # bp2 = np.inner(b,b)
        # crossab = np.cross(a,b)
        # crossabp2 = np.inner(crossab, crossab)

        # ccenter = np.cross(ap2*b - bp2*a, crossab) / (2 * crossabp2) + self.c.getCoords()
        # cradius = sqrt(ap2 * bp2 * np.inner(a-b,a-b)) / (2*sqrt(crossabp2))
        return(cradius, ccenter)


    def getCoords(self):
        return np.array([
            self.a.getCoords(),
            self.b.getCoords(),
            self.c.getCoords()
        ])

    def getPoints(self):
        return [self.a, self.b, self.c]

    def isPoint(self, point):
        for p in self.getPoints():
            if p == point:
                return True

    def getEdges(self):
        return [
                {self.a, self.b},
                {self.b, self.c},
                {self.c, self.a}
        ]

    def draw(self):
        t = plt.Polygon(self.getCoords()[:,0:2], fill=False)
        for p in self.getPoints():
            p.draw()
        # c = plt.Circle(list(self.ccenter[0:2]), self.cradius, fill=False)
        plt.gca().add_patch(t)
        # plt.gca().add_patch(c)

class Voronoi:
    def __init__(self, points):
        self.supertr = self.superTriang(points)
        self.triang = [self.supertr]
        self.points = points

        for p in points:
            self.addPoint(Point(p[0],p[1]))
            # self.draw()

    def addPoint(self, point):
        badT = []
        for t in self.triang:
            if point.inTriagCercumC(t):
                badT.append(t)

        # Find convex hull of badT
        polygon = []
        for t in badT:
            for edge in t.getEdges():
                if edge in polygon:
                    polygon.remove(edge)
                else:
                    polygon.append(edge)

        for t in badT: self.triang.remove(t)

        for edge in polygon:
            edge = list(edge)
            self.triang.append(Triangle(point, edge[0], edge[1]))

    def superTriang(self, points):
        points = np.array(points)
        xmax = max(points[:,0])
        ymax = max(points[:,1])
        xmin = min(points[:,0])
        ymin = min(points[:,1])
        return Triangle(
            Point(2*xmin-xmax, ymin),
            Point(2*xmax-xmin, ymin),
            Point(xmax-(xmax-xmin)/2, 2*ymax)
        )

    def draw(self):
        plt.figure()
        plt.grid(True, which='both')
        for t in self.triang:
            t.draw()

        plt.show()




