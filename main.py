from copy import deepcopy


class Matrix:
    def __init__(self, matrix_):
        self.matrix = deepcopy(matrix_)
        self.len_str = len(matrix_)
        self.len_slb = len(matrix_[0])

    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(f"{i:6}", end="")
            print()
        return ""
    def __add__(self, other: "Matrix")-> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError

        for x in range(self.len_str):
            for y in range(self.len_slb):

                self.matrix[x][y] = self.matrix[x][y] + other.matrix[x][y]
        return self


    def __mul__(self, other: "Matrix")-> "Matrix":
        if isinstance(other, (int, float)):

            return Matrix([[i * other for i in list] for list in self.matrix])
        elif isinstance(other, Matrix):

            for x in range(len(other.matrix[0])):
                for y in range(len(other.matrix)):
                    self.matrix[x][y] = self.matrix[x][y] * other.matrix[x][y]

            return self



if __name__ == '__main__':
    m = Matrix([[10, 1000, 20], [0, 0, 1], [1, 1, 10]])
    n = Matrix([[10, 20, 30], [40, 50, 1], [1, 1, 10]])

    print(m)
    print(m.len_slb)
    print(m.len_str)
    print(m+n)
    print(m * 5)
    print(m * n)
