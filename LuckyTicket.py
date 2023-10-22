from abc import ABC, abstractmethod


class ITask(ABC):
    @abstractmethod
    def run(self, input_data):
        pass


def count_lucky_tickets6():
    count = 0
    for a_1 in range(10):
        for a_2 in range(10):
            for a_3 in range(10):
                sumA = a_1 + a_2 + a_3
                for b_1 in range(10):
                    for b_2 in range(10):
                        b_3 = sumA - b_1 - b_2
                        if b_3 <= 9 and b_3 >= 0:
                            count += 1
    return count


def sum_of_digits(number):
    sum_of_digits_val = 0
    while number > 0:
        sum_of_digits_val += number % 10
        number //= 10
    return sum_of_digits_val


class LuckyTickets(ITask):
    def __init__(self):
        self.count = 0
        self.count_combinations = 0

    def run(self, input_data):
        n = int(input_data[0])
        self.count = 0
        self.getluckyfast(n)
        # self.getluckycountrec(n, 0, 0)
        return str(self.count)

    def run_old(self, n):
        self.count = 0
        self.getluckyfast(n)
        # self.getluckycountrec(n, 0, 0)
        # self.getluckycountloop(n)
        return self.count

    def getluckycountloop(self, n):
        # brute force solution
        for i in range(10**(2*n)):
            sumA = 0
            sumB = 0
            for j in range(n):
                sumA += i // (10 ** j) % 10
            for j in range(n, 2 * n):
                sumB += i // (10 ** j) % 10
            if sumA == sumB:
                self.count += 1

    def getluckycountrec(self, n, sumA, sumB):
        # recursive solution
        if n == 0:
            if sumA == sumB:
                self.count += 1
            return

        for a in range(10):
            for b in range(10):
                self.getluckycountrec(n - 1, sumA + a, sumB + b)

    def getluckyfast(self, n):
        """
        analytical or analytical/numerical solution

        (ab) (xy)
        a+b  #   combinations
        0    1   00
        1    2   01 10
        2    3   02 11 20
        3    4   03 12 21 30
        4
        ...
        18

        x+y  #   combinations
        0    1   00
        1    2   01 10
        2    3   02 11 20
        3    4   03 12 21 30
        4
        ...
        18

        if a+b = 3 then # tickets s.t. a+b == x+y is 16
        0303 0312 0321 0330
        1203 1212 1221 1230
        2103 2112 2121 2130
        3003 3012 3021 3030

        for each possible sum: 0 ... 9 * n,
        we can find the number of combinations smart way
        but also using brute force (by checking all possible combinations)

        :return:
        """
        for i in range(9 * n + 1):
            # compute number of combinations: brute force
            count_comb = 0
            for j in range(10**n):
                if sum_of_digits(j) == i:
                    count_comb += 1
            self.count += self.count_combinations * self.count_combinations

            # compute number of combinations: smart way
            # self.count_combinations = 0
            # self.count_combinations_apply(n, i)
            #
            # self.count += self.count_combinations * self.count_combinations

    def count_combinations_apply(self, n, sum):
        if n == 1:
            if sum > -1:
                self.count_combinations += 1
            return

        for j in range(10):
            self.count_combinations_apply(n - 1, sum - j)


class CountCombinations:
    def __init__(self):
        self.count = 0

    def count_combinations(self, n, sum):
        if n == 1:
            if sum > -1:
                self.count += 1
            return

        for j in range(10):
            self.count_combinations(n - 1, sum - j)


if __name__ == '__main__':
    n = 1
    for i in range(1, n + 1):
        cc = CountCombinations()
        cc.count_combinations(n, i)
        print(cc.count)

    lucky_tickets = LuckyTickets()
    for n in range(1, 6):
        res = lucky_tickets.run_old(n)
        print(f'n: {n}, # lucky tickets: {res}')
