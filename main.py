from copy import deepcopy


class Matrix:
    def __init__(self, matrix_):
        self.matrix = deepcopy(matrix_)
        self.len_str = len(matrix_[0])
        self.len_slb = len(matrix_)

    def __str__(self):
        print("_" * len(self.matrix[0]) * 6)
        for row in self.matrix:
            for i in row:
                print(f"{i:6}", end="")
            print()
        return "_" * len(self.matrix[0]) * 6


    def __add__(self, other: "Matrix")-> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError
        if not (len(other.matrix[0]) == len(self.matrix[0]) and len(other.matrix) == len(self.matrix)):
            raise IndexError
        for x in range(self.len_str):
            for y in range(self.len_slb):
                self.matrix[x][y] = self.matrix[x][y] + other.matrix[x][y]
        return self


    def __mul__(self, other: "Matrix")-> "Matrix":
        if isinstance(other, (int, float)):
            return Matrix([[i * other for i in list] for list in self.matrix])
        elif isinstance(other, Matrix) and len(other.matrix) == self.len_str:
            s = Matrix([other.matrix[0]] * len(self.matrix))*0
            for x in range(len(self.matrix)):
                for y in range(len(other.matrix[0])):
                    for a in range(len(other.matrix)):
                        s.matrix[x][y] += self.matrix[x][a] * other.matrix[a][y]
            return s






if __name__ == '__main__':
    m = Matrix([[10, 150, 20], [0, 0, 1], [1, 1, 10]])
    n = Matrix([[10, 20, 30], [40, 50, 1], [1, 1, 10]])
    z = Matrix([[10, 100, 20, 40], [0, 0, 1, 2], [1, 1, 10, 1], [1, 2, 3, 4]])
    a = Matrix([[1, 2, 3], [3, 4, 5]])
    b = Matrix([[5, 6], [7, 8], [7, 9]])
    #print(z)
    #print(m)
    #print(m.len_slb)
    #print(m.len_str)
    print(m + n)
    #print(m * 5)
    print(m * n)
    print(a * b)