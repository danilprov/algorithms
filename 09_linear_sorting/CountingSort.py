from ISort import ISort


class CountingSort(ISort):
    def __init__(self, array, func=lambda x: x):
        super().__init__(array)
        self.func = func

    def find_max(self):
        max_value = self.func(self.array[0])
        for i in range(1, self.N):
            if self.func(self.array[i]) > max_value:
                max_value = self.func(self.array[i])

        return max_value

    def sort(self):
        max_value = self.find_max()
        self.bucket = [0] * (max_value + 1)
        for i in range(self.N):
            self.bucket[self.func(self.array[i])] += 1
        for j in range(1, max_value + 1):
            self.bucket[j] = self.bucket[j] + self.bucket[j - 1]
        sorted_array = [None] * self.N
        for i in range(self.N - 1, -1, -1):
            self.bucket[self.func(self.array[i])] -= 1
            right_idx = self.bucket[self.func(self.array[i])]
            sorted_array[right_idx] = self.array[i]
        self.array = sorted_array


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

    sort = CountingSort(a)
    start_time = time.time() * 1000.
    sort.sort()
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)
