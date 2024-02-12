from ISort import ISort


class InsertionSort(ISort):
    def sort(self, left, right):
        """
        swaps a target element until its place is found in the sorted part and inserts it there
        :return:
        """
        for i in range(1, self.N):
            j = i - 1
            while j >= 0 and self.more(j, j + 1):
                self.swap(j, j + 1)
                j -= 1


class InsertionSortShift(ISort):
    def sort(self, left, right):
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


class InsertionSortBinarySearch(ISort):
    def sort(self, left, right):
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

    sort = InsertionSortBinarySearch(create_array(100))
    start_time = time.time() * 1000.
    sort.sort(0, sort.N - 1)
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)
    print(sort.toString())