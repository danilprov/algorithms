class Matrix2D():
    def __init__(self, a, b, c, d):
        self.matrix = [[a, b], [c, d]]
        self.num_rows = 2
        self.num_columns = 2

    def get_element(self, i, j):
        return self.matrix[i][j]

    def assign_element(self, value, i, j):
        self.matrix[i][j] = value

    def multiply(self, matrix):
        result = Matrix2D(0, 0, 0, 0)
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                sum = 0
                for k in range(self.num_rows):
                    sum += self.get_element(i, k) * matrix.get_element(k, j)

                result.assign_element(sum, i, j)

        return result

    def print(self):
        for i in range(self.num_rows):
            print(self.matrix[i])


if __name__ == '__main__':
    a = Matrix2D(1, 0, 0, 1)
    b = Matrix2D(5, 3, 3, 2)
    c = Matrix2D(1, 1, 1, 0)

    a_ = a.multiply(b)
    b_ = b.multiply(b)
    c_ = c.multiply(b)
    print(a_.print())
    print(b_.print())
    print(c_.print())
