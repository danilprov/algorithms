from ISort import ISort


class QuickSort(ISort):
    """
    Original quicksort algorithm proposed by Hoera.
    Since pivot is not guaranteed to end up in its final place after split,
    the left recursion call involves pivot as well.
    """
    def split(self, left, right):
        pivot = self.array[right]
        j = right
        i = left
        while True:
            #while self.array[i] <= pivot and i < right:
            while not self.moreK(i, pivot) and (i < right):
                i += 1
            #while self.array[j] > pivot and j > left:
            while self.moreK(j, pivot) and j > left:
                j -= 1
            if i < j:
                self.swap(i, j)
            else:
                break

        return i - 1

    def sort(self, left, right):
        if left >= right:
            return

        m = self.split(left, right)
        self.sort(left, m)
        self.sort(m + 1, right)


class QuickSortLomuto(ISort):
    """
    Quicksort algorithm using Lomuto partition scheme.
    More elegant as pivot ends up in its final place after split.
    Less efficient than the original scheme when all elements are equal.
    """
    def split(self, left, right):
        m = left - 1
        pivot = self.array[right]
        for j in range(left, right + 1):
            #if self.array[j] <= pivot:
            if not self.moreK(j, pivot):
                m += 1
                self.swap(m, j)

        return m

    def sort(self, left, right):
        if left >= right:
            return

        m = self.split(left, right)
        self.sort(left, m - 1)
        self.sort(m + 1, right)


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

    sort = QuickSort(a)
    start_time = time.time() * 1000.
    sort.sort(0, sort.N - 1)
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)
    print(sort.toString())