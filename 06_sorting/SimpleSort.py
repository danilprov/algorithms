import random


class Sort():
    def __init__(self, array):
        self.array = array
        self.N = len(array)
        self.cmp = 0
        self.asg = 0

    def Bubble(self):
        for i in range(1, self.N):
            for j in range(self.N - i):
                if self.more(j, j + 1):
                    self.swap(j, j + 1)

    def Insertion(self):
        """
        swaps a target element until its place is found in the sorted part and inserts it there
        :return:
        """
        for i in range(1, self.N):
            j = i - 1
            while j >= 0 and self.more(j, j + 1):
                self.swap(j, j + 1)
                j -= 1

    def InsertionShift(self):
        """
        instead of swaping a target element n times (where n is distance to its place),
        InsertionShift stores the element to some variable and shifts n-1 elements before
        the target element to the right, then puts the target element to its place.

        The cost of swaping is 3n, whereas the cost of storing shifting and putting is n + 2.
        :return:
        """
        for i in range(1, self.N):
            k = self.array[i]
            self.asg += 1
            j = i - 1
            while j >= 0 and self.moreK(j, k):
                self.array[j + 1] = self.array[j]
                self.asg += 1
                j -= 1
            self.array[j + 1] = k
            self.asg += 1

    def InsertionBinarySearch(self):
        """
        instead of swaping a target element n times (where n is distance to its place),
        InsertionShift stores the element to some variable and shifts n-1 elements before
        the target element to the right, then puts the target element to its place.

        The cost of swaping is 3n, whereas the cost of storing shifting and putting is n + 2.
        :return:
        """
        for i in range(1, self.N):
            k = self.array[i]
            self.asg += 1
            j = i - 1
            p = self.binarySearch(k, 0, i - 1)
            while j >= p:
                self.array[j + 1] = self.array[j]
                self.asg += 1
                j -= 1
            # for j in range(i - 1, p - 1, -1):
            #     self.array[j + 1] = self.array[j]
            #     self.asg += 1
            self.array[p] = k
            self.asg += 1

    def binarySearch(self, k, left, right):
        while right > left:
            midpoint = (right + left) // 2
            self.cmp += 1
            if k >= self.array[midpoint]:
                left = midpoint + 1
            else:
                right = midpoint - 1
        self.cmp += 1
        if k > self.array[left]:
            return left + 1
        else:
            return left

    def binarySearchRec(self, k, left, right):
        if right <= left:
            if k > self.array[left]:
                return left + 1
            else:
                return left
        midpoint = (right + left) // 2
        self.cmp += 1
        if k > self.array[midpoint]:
            return self.binarySearchRec(k, midpoint + 1, right)
        else:
            return self.binarySearchRec(k, left, midpoint - 1)

    def Shell(self):
        """
        It's easier to read its description on wikipedia (https://en.wikipedia.org/wiki/Shellsort),
        but basically it starts by sorting sets of elements that are located far from each other
        using Buble or Insertion sort, and then progressively reduces the gap.

        :return:
        """
        gap = self.N // 2
        while gap > 0:
            for i in range(gap, self.N):
                j = i
                while j >= gap and self.more(j - gap, j):
                    self.swap(j, j - gap)
                    j -= gap
            gap //= 2

    def Selection(self):
        for i in range(1, self.N):
            x = self.findMax(self.N - i + 1)
            self.swap(x, self.N - i)

    def findMax(self, size):
        x = 0
        for i in range(size):
            self.cmp += 1
            if self.array[i] > self.array[x]:
                x = i
        return x

    def swap(self, i, j):
        self.asg += 3
        x = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = x

    def more(self, i, j):
        self.cmp += 1
        return self.array[i] > self.array[j]

    def moreK(self, i, k):
        self.cmp += 1
        return self.array[i] > k

    def toString(self):
        return f'N:  {self.N} \ncmp: {self.cmp} \nasg: {self.asg}'


if __name__ == '__main__':
    import random
    import time

    def create_array(size, replacement=True):
        array = list(range(size))
        random.seed(12345)
        if replacement:
            return [random.choice(array) for _ in range(len(array))]
        else:
            random.shuffle(array)
            return array

    a = [5, 3, 7, 4, 2, 9, 1, 0, 6, 8]
    r = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    sort = Sort(create_array(100000))
    #print(sort.array)
    start_time = time.time() * 1000.
    sort.Selection()
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    #print(sort.array)
    print(sort.toString())
