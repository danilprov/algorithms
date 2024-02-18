from CountingSort import CountingSort
from ISort import ISort


class RadixSort(ISort):
    def __init__(self, array, num_digits=10):
        super().__init__(array)
        self.num_digits = num_digits

    def sort(self):
        max_value = self.find_max()
        l = 0
        while max_value > 0:
            sort_radix = CountingSort(self.array, lambda x: x // 10 ** l % 10)
            sort_radix.sort()
            self.array = sort_radix.array
            l += 1
            max_value = max_value // 10

    def find_max(self):
        max_value = self.array[0]
        for i in range(1, self.N):
            if self.array[i] > max_value:
                max_value = self.array[i]

        return max_value


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

    a = [53, 34, 32, 43, 24, 98, 10, 0, 63, 89]
    r = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    sort = RadixSort(create_array(999))
    start_time = time.time() * 1000.
    sort.sort()
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)