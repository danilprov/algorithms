class QuickMergeSort:
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

    def quick_sort(self, left, right):
        if left >= right:
            return

        m = self.split(left, right)
        self.quick_sort(left, m - 1)
        self.quick_sort(m + 1, right)

    def merge(self, left, mid, right):
        temp_array = [0] * (right - left + 1)
        i = left
        j = mid + 1
        x = 0

        # merge two parts in the right order
        while (i <= mid) and (j <= right):
            if self.array[i] <= self.array[j]:
                temp_array[x] = self.array[i]
                i += 1
                x += 1
            else:
                temp_array[x] = self.array[j]
                j += 1
                x += 1
        while i <= mid:
            temp_array[x] = self.array[i]
            i += 1
            x += 1
        while j <= right:
            temp_array[x] = self.array[j]
            j += 1
            x += 1

        # copy sorted temp_array back to self.array in the right place
        for k in range(left, right + 1):
            self.array[k] = temp_array[k - left]
        del temp_array

    def merge_sort(self, left, right):
        if left >= right:
            return

        mid = int((left + right) / 2)
        self.merge_sort(left, mid)
        self.merge_sort(mid + 1, right)
        self.merge(left, mid, right)


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

    sort = QuickMergeSort(a)
    start_time = time.time() * 1000.
#    sort.quick_sort(0, sort.N - 1)
    sort.merge_sort(0, sort.N - 1)
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)

    # sort.array = [2, 3, 5, 1, 3, 6]
    # sort.merge(0, 2, 5)
    # print(sort.array)

