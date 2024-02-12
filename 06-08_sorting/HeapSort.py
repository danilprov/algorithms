from ISort import ISort


class HeapSort(ISort):
    def sort(self, left, right):
        # root can be found by this formula root = (N - 1 - 1) / 2
        for root in range(int((self.N - 1 - 1) / 2), -1, -1):
            self.heapify(root, self.N)

        for j in range(self.N - 1, 0, -1):
            self.swap(0, j)
            self.heapify(0, j)

    def heapify(self, root, size):
        """move max to root"""
        # find root children (left and right elements)
        L = 2 * root + 1
        R = L + 1

        # compare triples and find max element
        X = root
        if L < size and self.array[L] > self.array[X]:
            X = L
        if R < size and self.array[R] > self.array[X]:
            X = R
        self.cmp += 2
        # if nothing changed we can stop
        if X == root:
            return
        # put max to the root
        self.swap(X, root)
        # call recursion for next level
        self.heapify(X, size)


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

    sort = HeapSort(create_array(100))
    start_time = time.time() * 1000.
    sort.sort(0, sort.N - 1)
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)
    print(sort.toString())