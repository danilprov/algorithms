import math

from Matrix2D import Matrix2D
from Power import PowerCalculator


class FibonacciCalculator():
    phi = (1 + math.sqrt(5)) / 2

    def fibonacci_rec(self, n):
        # recurssion - O(2^n) algrorithm for fibonacci
        if n <= 1:
            return n

        return self.fibonacci_rec(n - 1) + self.fibonacci_rec(n - 2)

    def fibonacci_loop(self, n):
        # loop - O(n) algorithm for fibonacci
        if n <= 1:
            return n

        f_pred1 = 1
        f_pred2 = 0

        for i in range(2, n + 1):
            f_cur = f_pred1 + f_pred2
            f_pred2 = f_pred1
            f_pred1 = f_cur

        return f_cur

    def fibonacci_gr(self, n):
        # golden ratio - algorithmically O(log(n)) but not practical
        # (involves operations with irrational numbers)
        return int(math.pow(FibonacciCalculator.phi, n) / math.sqrt(5) + 1 / 2)

    def fibonacci_matmul(self, n):
        # matrix multiplication for fibonacci - O(log(n)) and practical
        # 1 1 x  f2 f1 = f2+f1 f1+f0  = f3 f2
        # 1 0    f1 f0   f2    f1       f2 f1

        # (1 1)^(N-1) = fn   fn-1
        # (1 0)         fn-1 fn-2
        base_matrix = Matrix2D(1, 1, 1, 0)
        power_calc = PowerCalculator()
        return power_calc.power_matrix_lnn(base_matrix, n-1)


if __name__ == '__main__':
    import time

    fibonacci_calc = FibonacciCalculator()

    def apply_method(method_name):
        return getattr(fibonacci_calc, method_name)

    methods = ['fibonacci_matmul', 'fibonacci_loop','fibonacci_rec',] #'fibonacci_gr',
    # for 'fibonacci_gr' returns "math range error" for n > 1000

    for method in methods:
        print(f'==== {method} ====')
        for i in range(1, 7):
            n = 10**i
            start_time = time.time() * 1000.
            fib_number = apply_method(method_name=method)(n)
            print(f'n = {n}; time spent - {round(time.time() * 1000. - start_time)} ms')
        print('\n')

    res = fibonacci_calc.fibonacci_matmul(6)

    print(res)