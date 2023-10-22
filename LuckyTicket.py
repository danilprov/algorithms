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


class LuckyTickets(ITask):
    def __init__(self):
        self.count = 0

    def run(self, input_data):
        n = int(input_data[0])
        self.count = 0
        self.getluckycountrec(n, 0, 0)
        return str(self.count)

    def run_old(self, n):
        self.count = 0
        #self.getluckycountrec(n, 0, 0)
        self.getluckycountloop(n)
        return self.count

    def getluckycountloop(self, n):
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
        if n == 0:
            if sumA == sumB:
                self.count += 1
            return

        for a in range(10):
            for b in range(10):
                self.getluckycountrec(n-1, sumA+a, sumB+b)

    def getluckyfast(self):
        """
        (ab) (xy)
        a+b  #   possibilities
        0    1   00
        1    2   01 10
        2    3   02 11 20
        3    4   03 12 21 30
        4
        ...
        18

        x+y  #   possibilities
        0    1   00
        1    2   01 10
        2    3   02 11 20
        3    4   03 12 21 30
        4
        ...
        18

        if a+b = 3 then # tickets s.t. a+b == x+y - 16
        0303 0312 0321 0330
        1203 1212 1221 1230
        2103 2112 2121 2130
        3003 3012 3021 3030
        :return:
        """
        pass


if __name__ == '__main__':
    lucky_tickets = LuckyTickets()
    for n in range(1, 5):
        res = lucky_tickets.run(n)
        print(f'n: {n}, # lucky tickets: {res}')
