from Matrix2D import Matrix2D


class PowerCalculator():
    def power(self, a, n):
        result = 1
        for i in range(n):
            result *= a

        return result

    def power_lnn(self, a, n):
        d = a
        p = 1
        while n > 1:
            n //= 2
            d *= d
            if n % 2 == 1:
                p *= d

        return p

    def power_matrix_lnn(self, matrix: Matrix2D, n: int):
        d = matrix
        if n % 2 == 1:
            p = matrix
        else:
            p = Matrix2D(1, 0, 0, 1)
        while n > 1:
            n //= 2
            d = d.multiply(d)
            if n % 2 == 1:
                p = p.multiply(d)

        return p.get_element(0, 0)
