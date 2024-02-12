from ISort import ISort


class SelectionSort(ISort):
    def sort(self, left, right):
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

    sort = SelectionSort(create_array(100))
    start_time = time.time() * 1000.
    sort.sort(0, sort.N - 1)
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)
    print(sort.toString())