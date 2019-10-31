import math, random

class rubicsCube:
    def __init__(self):
        self.faces = [
            [['white', 'white', 'white'], ['white', 'white', 'white'], ['white', 'white', 'white']],
            [['red', 'red', 'red'], ['red', 'red', 'red'], ['red', 'red', 'red']],
            [['blue', 'blue', 'blue'], ['blue', 'blue', 'blue'], ['blue', 'blue', 'blue']],
            [['green', 'green', 'green'], ['green', 'green', 'green'], ['green', 'green', 'green']],
            [['orange', 'orange', 'orange'], ['orange', 'orange', 'orange'], ['orange', 'orange', 'orange']],
            [['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow'], ['yellow', 'yellow', 'yellow']]
            ]

        self.points = [[-1.5, 1.5, -1.5], [-1.5, 1.5, -0.5], [-1.5, 1.5, 0.5], [-1.5, 1.5, 1.5], [-0.5, 1.5, -1.5], [-0.5, 1.5, -0.5], [-0.5, 1.5, 0.5], [-0.5, 1.5, 1.5], [0.5, 1.5, -1.5], [0.5, 1.5, -0.5], [0.5, 1.5, 0.5], [0.5, 1.5, 1.5], [1.5, 1.5, -1.5], [1.5, 1.5, -0.5], [1.5, 1.5, 0.5], [1.5, 1.5, 1.5],
                       [-1.5, -1.5, -1.5], [-1.5, -0.5, -1.5], [-1.5, 0.5, -1.5], [-1.5, 1.5, -1.5], [-0.5, -1.5, -1.5], [-0.5, -0.5, -1.5], [-0.5, 0.5, -1.5], [-0.5, 1.5, -1.5], [0.5, -1.5, -1.5], [0.5, -0.5, -1.5], [0.5, 0.5, -1.5], [0.5, 1.5, -1.5], [1.5, -1.5, -1.5], [1.5, -0.5, -1.5], [1.5, 0.5, -1.5], [1.5, 1.5, -1.5],
                       [1.5, -1.5, -1.5], [1.5, -0.5, -1.5], [1.5, 0.5, -1.5], [1.5, 1.5, -1.5], [1.5, -1.5, -0.5], [1.5, -0.5, -0.5], [1.5, 0.5, -0.5], [1.5, 1.5, -0.5], [1.5, -1.5, 0.5], [1.5, -0.5, 0.5], [1.5, 0.5, 0.5], [1.5, 1.5, 0.5], [1.5, -1.5, 1.5], [1.5, -0.5, 1.5], [1.5, 0.5, 1.5], [1.5, 1.5, 1.5],
                       [1.5, -1.5, 1.5], [1.5, -0.5, 1.5], [1.5, 0.5, 1.5], [1.5, 1.5, 1.5], [0.5, -1.5, 1.5], [0.5, -0.5, 1.5], [0.5, 0.5, 1.5], [0.5, 1.5, 1.5], [-0.5, -1.5, 1.5], [-0.5, -0.5, 1.5], [-0.5, 0.5, 1.5], [-0.5, 1.5, 1.5], [-1.5, -1.5, 1.5], [-1.5, -0.5, 1.5], [-1.5, 0.5, 1.5], [-1.5, 1.5, 1.5],
                       [-1.5, -1.5, 1.5], [-1.5, -0.5, 1.5], [-1.5, 0.5, 1.5], [-1.5, 1.5, 1.5], [-1.5, -1.5, 0.5], [-1.5, -0.5, 0.5], [-1.5, 0.5, 0.5], [-1.5, 1.5, 0.5], [-1.5, -1.5, -0.5], [-1.5, -0.5, -0.5], [-1.5, 0.5, -0.5], [-1.5, 1.5, -0.5], [-1.5, -1.5, -1.5], [-1.5, -0.5, -1.5], [-1.5, 0.5, -1.5], [-1.5, 1.5, -1.5],
                       [-1.5, -1.5, 1.5], [-1.5, -1.5, 0.5], [-1.5, -1.5, -0.5], [-1.5, -1.5, -1.5], [-0.5, -1.5, 1.5], [-0.5, -1.5, 0.5], [-0.5, -1.5, -0.5], [-0.5, -1.5, -1.5], [0.5, -1.5, 1.5], [0.5, -1.5, 0.5], [0.5, -1.5, -0.5], [0.5, -1.5, -1.5], [1.5, -1.5, 1.5], [1.5, -1.5, 0.5], [1.5, -1.5, -0.5], [1.5, -1.5, -1.5]]
        self.triangles = [[0, 1, 4], [1, 4, 5], [1, 2, 5], [2, 5, 6], [2, 3, 6], [3, 6, 7], [4, 5, 8], [5, 8, 9], [5, 6, 9],
                          [6, 9, 10], [6, 7, 10], [7, 10, 11], [8, 9, 12], [9, 12, 13], [9, 10, 13], [10, 13, 14], [10, 11, 14], [11, 14, 15],
                          [16, 17, 20], [17, 20, 21], [17, 18, 21], [18, 21, 22], [18, 19, 22], [19, 22, 23], [20, 21, 24], [21, 24, 25], [21, 22, 25],
                          [22, 25, 26], [22, 23, 26], [23, 26, 27], [24, 25, 28], [25, 28, 29], [25, 26, 29], [26, 29, 30], [26, 27, 30], [27, 30, 31],
                          [32, 33, 36], [33, 36, 37], [33, 34, 37], [34, 37, 38], [34, 35, 38], [35, 38, 39], [36, 37, 40], [37, 40, 41], [37, 38, 41],
                          [38, 41, 42], [38, 39, 42], [39, 42, 43], [40, 41, 44], [41, 44, 45], [41, 42, 45], [42, 45, 46], [42, 43, 46], [43, 46, 47],
                          [48, 49, 52], [49, 52, 53], [49, 50, 53], [50, 53, 54], [50, 51, 54], [51, 54, 55], [52, 53, 56], [53, 56, 57], [53, 54, 57],
                          [54, 57, 58], [54, 55, 58], [55, 58, 59], [56, 57, 60], [57, 60, 61], [57, 58, 61], [58, 61, 62], [58, 59, 62], [59, 62, 63],
                          [64, 65, 68], [65, 68, 69], [65, 66, 69], [66, 69, 70], [66, 67, 70], [67, 70, 71], [68, 69, 72], [69, 72, 73], [69, 70, 73],
                          [70, 73, 74], [70, 71, 74], [71, 74, 75], [72, 73, 76], [73, 76, 77], [73, 74, 77], [74, 77, 78], [74, 75, 78], [75, 78, 79],
                          [80, 81, 84], [81, 84, 85], [81, 82, 85], [82, 85, 86], [82, 83, 86], [83, 86, 87], [84, 85, 88], [85, 88, 89], [85, 86, 89],
                          [86, 89, 90], [86, 87, 90], [87, 90, 91], [88, 89, 92], [89, 92, 93], [89, 90, 93], [90, 93, 94], [90, 91, 94], [91, 94, 95]]

    @property
    def readPoints(self):
        return self.points
    
    @property
    def readTriangles(self):
        triangles = []
        for z, face in enumerate(self.faces):
            for y, row in enumerate(face):
                for x, column in enumerate(row):
                    i1 = z * 18 + y * 6 + x * 2
                    i2 = i1 + 1
                    triangle = self.triangles[i1] + [self.faces[z][y][x]]
                    triangles.append(triangle)
                    triangle = self.triangles[i2] + [self.faces[z][y][x]]
                    triangles.append(triangle)

        return triangles

    def rotate(self, face):
        self.faces[face] = [[self.faces[face][0][2], self.faces[face][1][2], self.faces[face][2][2]],
                            [self.faces[face][0][1], self.faces[face][1][1], self.faces[face][2][1]],
                            [self.faces[face][0][0], self.faces[face][1][0], self.faces[face][2][0]]]

    def randomize(self, iterations):
        for x in range(iterations):
            exec('self.' + ['U', 'D', 'F', 'B', 'R', 'L'][random.randint(0,5)])

    @property
    def U(self):
        self.rotate(0)
        (
        self.faces[1][2][2], self.faces[1][1][2], self.faces[1][0][2],
        self.faces[2][2][2], self.faces[2][1][2], self.faces[2][0][2],
        self.faces[3][2][0], self.faces[3][2][1], self.faces[3][2][2],
        self.faces[4][2][2], self.faces[4][1][2], self.faces[4][0][2]
        ) = (
        self.faces[4][2][2], self.faces[4][1][2], self.faces[4][0][2],
        self.faces[1][2][2], self.faces[1][1][2], self.faces[1][0][2],
        self.faces[2][2][2], self.faces[2][1][2], self.faces[2][0][2],
        self.faces[3][2][0], self.faces[3][2][1], self.faces[3][2][2]
        )

    @property
    def D(self):
        self.rotate(5)
        (
        self.faces[1][0][0], self.faces[1][1][0], self.faces[1][2][0],
        self.faces[4][0][0], self.faces[4][1][0], self.faces[4][2][0],
        self.faces[3][0][2], self.faces[3][0][1], self.faces[3][0][0],
        self.faces[2][0][0], self.faces[2][1][0], self.faces[2][2][0]
        ) = (
        self.faces[2][0][0], self.faces[2][1][0], self.faces[2][2][0],
        self.faces[1][0][0], self.faces[1][1][0], self.faces[1][2][0],
        self.faces[4][0][0], self.faces[4][1][0], self.faces[4][2][0],
        self.faces[3][0][2], self.faces[3][0][1], self.faces[3][0][0],
        )

    @property
    def F(self):
        self.rotate(1)
        (
        self.faces[0][0][0], self.faces[0][1][0], self.faces[0][2][0],
        self.faces[4][2][0], self.faces[4][2][1], self.faces[4][2][2],
        self.faces[5][2][2], self.faces[5][1][2], self.faces[5][0][2],
        self.faces[2][0][2], self.faces[2][0][1], self.faces[2][0][0]
        ) = (
        self.faces[2][0][2], self.faces[2][0][1], self.faces[2][0][0],
        self.faces[0][0][0], self.faces[0][1][0], self.faces[0][2][0],
        self.faces[4][2][0], self.faces[4][2][1], self.faces[4][2][2],
        self.faces[5][2][2], self.faces[5][1][2], self.faces[5][0][2]
        )
    
    @property
    def B(self):
        self.rotate(3)
        (
        self.faces[0][2][2], self.faces[0][1][2], self.faces[0][0][2],
        self.faces[2][2][0], self.faces[2][2][1], self.faces[2][2][2],
        self.faces[5][0][0], self.faces[5][1][0], self.faces[5][2][0],
        self.faces[4][0][2], self.faces[4][0][1], self.faces[4][0][0]
        ) = (
        self.faces[4][0][2], self.faces[4][0][1], self.faces[4][0][0],
        self.faces[0][2][2], self.faces[0][1][2], self.faces[0][0][2],
        self.faces[2][2][0], self.faces[2][2][1], self.faces[2][2][2],
        self.faces[5][0][0], self.faces[5][1][0], self.faces[5][2][0]
        )
        
    @property
    def R(self):
        self.rotate(4)
        (
        self.faces[0][0][2], self.faces[0][0][1], self.faces[0][0][0],
        self.faces[3][0][0], self.faces[3][1][0], self.faces[3][2][0],
        self.faces[5][0][2], self.faces[5][0][1], self.faces[5][0][0],
        self.faces[1][0][2], self.faces[1][0][1], self.faces[1][0][0]
        ) = (
        self.faces[1][0][2], self.faces[1][0][1], self.faces[1][0][0],
        self.faces[0][0][2], self.faces[0][0][1], self.faces[0][0][0],
        self.faces[3][0][0], self.faces[3][1][0], self.faces[3][2][0],
        self.faces[5][0][2], self.faces[5][0][1], self.faces[5][0][0]
        )

    @property
    def L(self):
        self.rotate(2)
        (
        self.faces[0][2][0], self.faces[0][2][1], self.faces[0][2][2],
        self.faces[1][2][0], self.faces[1][2][1], self.faces[1][2][2],
        self.faces[5][2][0], self.faces[5][2][1], self.faces[5][2][2],
        self.faces[3][2][2], self.faces[3][1][2], self.faces[3][0][2]
        ) = (
        self.faces[3][2][2], self.faces[3][1][2], self.faces[3][0][2],
        self.faces[0][2][0], self.faces[0][2][1], self.faces[0][2][2],
        self.faces[1][2][0], self.faces[1][2][1], self.faces[1][2][2],
        self.faces[5][2][0], self.faces[5][2][1], self.faces[5][2][2]
        )
