from Task import ITask


# warm up: naive solution that works only for n=6
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

# some auxiliary f-n: we will need it later
def sum_of_digits(number):
    sum_of_digits_val = 0
    while number > 0:
        sum_of_digits_val += number % 10
        number //= 10
    return sum_of_digits_val


class LuckyTickets(ITask):
    def __init__(self):
        self.count = 0

    def run(self, input_data):
        n = int(input_data)
        self.count = 0
        self.getluckyfast(n)
        # self.getluckycountrec(n, 0, 0)
        return str(self.count)

    # brute force solution for generic n using for loop: complexity is O(10^(2n)) = O(100^n)
    def getluckycountloop(self, n):
        # brute force solution
        for i in range(10 ** (2 * n)):
            sumA = 0
            sumB = 0
            for j in range(n):
                sumA += i // (10 ** j) % 10
            for j in range(n, 2 * n):
                sumB += i // (10 ** j) % 10
            if sumA == sumB:
                self.count += 1

    # brute force solution for generic n using recursion: complexity is O((10*10)^n) = O(100^n)
    def getluckycountrec(self, n, sumA, sumB):
        # recursive solution
        if n == 0:
            if sumA == sumB:
                self.count += 1
            return

        for a in range(10):
            for b in range(10):
                self.getluckycountrec(n - 1, sumA + a, sumB + b)

    # smart solution for generic n using # of combinations: complexity is O(n*9n*10) = O(90n^2) and O(n) space
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

        Implementation of the smart way:
        0. we create the result for n=1 manualy - `prev_num_of_comb` containing all 1's,
           this corresponds to # of combinations for each possible value of digit sum for current n
        1. To find # of combination for some n>1, we need to use `prev_num_of_comb` from n-1
           so, we first run a loop over all previous n's.
        2. In each inner loop,
            - we create `cur_num_of_comb`, where we store # of combinations for each possible
              value of digit_sum for current n. This container consists of 9 extra elements
              (9 * (i+1)) to ensure a smooth transition to n+1
            - for each possible value of `digit_sum`, we fill in `cur_num_of_comb` by running
              over all possible `last_digit` and adding the corresponding # of combinations
              from `prev_num_of_comb` - the result obtained for n-1. (here we fill only actual
              9 * i values, the rest 9 elements remain untouched)
            - the corresponding # of combinations from `prev_num_of_comb` are controlled by
              `if 0 <= digit_sum - last_digit` clause. So we either sum over 10 elements preceding
              the current `digit_sum` value, or we stop the summation earlier if the index becomes negative

        :return:
        """
        prev_num_of_comb = [1] * 10 + [0] * 9

        for i in range(2, n + 1):
            cur_num_of_comb = [0] * (9 * (i + 1) + 1)
            for digit_sum in range(9 * i + 1):
                for last_digit in range(10):
                    if 0 <= digit_sum - last_digit:
                        cur_num_of_comb[digit_sum] += prev_num_of_comb[digit_sum - last_digit]
            prev_num_of_comb = cur_num_of_comb

        for i in range(len(prev_num_of_comb)):
            self.count += prev_num_of_comb[i] * prev_num_of_comb[i]


if __name__ == '__main__':
    # running naive solution
    print(count_lucky_tickets6())

    # running fast solution
    lucky_tickets = LuckyTickets()
    for n in range(1, 6):
        res = lucky_tickets.run(n)
        print(f'n: {n}, # lucky tickets: {res}')