class QuickSort:
    def __init__(self, array):
        self.array = array
        self.N = len(array)
        self.cmp = 0
        self.asg = 0

    def swap(self, left, right):
        x = self.array[left]
        self.array[left] = self.array[right]
        self.array[right] = x

    def split(self, left, right):
        m = left - 1
        pivot = self.array[right]
        for j in range(left, right+1):
            if self.array[j] <= pivot:
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
    #print(sort.toString())

