from ISort import ISort


class ShellSort(ISort):
    def sort(self, left, right):
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

    sort = ShellSort(create_array(100))
    start_time = time.time() * 1000.
    sort.sort(0, sort.N - 1)
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)
    print(sort.toString())