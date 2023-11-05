import time
import math


class PrimeNumbers():
    def __init__(self):
        self.primes = None

    def is_prime(self, p):
        # find number of factors for a given number p
        count = 0
        for i in range(1, p + 1):
            if p % i == 0:
                count += 1
        return count == 2

    def is_prime2(self, p):
        # check if number of factors between 2 and p-1 is 0
        for i in range(2, p):
            if p % i == 0:
                return False
        return True

    def is_prime3(self, p):
        # check if number of factors between 2 and p // 2 is 0
        for i in range(2, p // 2 + 1):
            if p % i == 0:
                return False
        return True

    def is_prime4(self, p):
        # check if number of factors between 2 and p // 2 is 0 but only check odd numbers
        if p == 2:
            return True
        if p % 2 == 0:
            return False
        for i in range(3, p // 2 + 1, 2):
            if p % i == 0:
                return False
        return True

    def is_prime5(self, p):
        # check if number of factors between 2 and sqrt(p) is 0 but only check odd numbers
        if p == 2:
            return True
        if p % 2 == 0:
            return False

        # this while loop is analogue of for loop below, but without using sqrt
        # i = 3
        # while i * i <= p:
        #     if p % i == 0:
        #         return False
        #     d += 2

        for i in range(3, int(math.sqrt(p)) + 1, 2):
            if p % i == 0:
                return False

        return True

    def count_primes(self, n):
        count = 0
        for p in range(2, n + 1):
            if self.is_prime5(p):
                count += 1

        return count

    def count_primes2(self, n):
        count = 1
        self.primes = []
        self.primes.append(2)
        for p in range(3, n + 1):
            if self.is_prime6(p):
                self.primes.append(p)
                count += 1

        return count

    def is_prime6(self, p):
        # check if number of factors between 2 and sqrt(p) is 0 but only check prime numbers
        if p == 2:
            return True
        if p % 2 == 0:
            return False
        s = p ** 0.5
        i = 0
        while self.primes[i] <= s:
            if p % self.primes[i] == 0:
                return False
            i += 1
        return True


if __name__ == '__main__':
    primes = PrimeNumbers()
    print(f'==== Odd numbers under sqrt(n) | O(n sqrt(n))====')
    for i in range(1, 8):
        n = 10 ** i
        start_time = time.time() * 1000.
        print(f'n = {n}; # primes = {primes.count_primes(n)}; time spent - {round(time.time() * 1000. - start_time)} ms')
    print('\n')

    print(f'==== Prime numbers under sqrt(n) | O(n log(n))====')
    for i in range(1, 8):
        n = 10 ** i
        start_time = time.time() * 1000.
        print(f'n = {n}; # primes = {primes.count_primes2(n)}; time spent - {round(time.time() * 1000. - start_time)} ms')
    print('\n')


# complexity          O(N^2)    O(N^2)    O(N*N/2)  O(N*N/4)   O(N^3/2) O(NlogN)
# N	        Primes	  A1 (ms)	A2 (ms)   A3 (ms)	A4 (ms)	   A5 (ms)	A6 (ms)
# 10	      4	       0.03	     0.02	   0.03	     0.02	    0.02	0.02
# 100	      25	   0.37	     0.09	   0.14	     0.04	    0.04	0.04
# 1000	      168	   36.73	 5.08	   4	     1.38	    0.48	0.52
# 10000	      1229	   5721	     410	   228	     118	    6.31	8.5
# 100000	  9592	             31231	   15328	 8663	    125	    121
# 1000000	  78498					                            2207	2018
# 10000000	  664579					                        66992	45941
