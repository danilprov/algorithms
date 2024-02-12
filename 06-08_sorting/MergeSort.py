from ISort import ISort


class MergeSort(ISort):
    def merge(self, left, mid, right):
        temp_array = [0] * (right - left + 1)
        i = left
        j = mid + 1
        x = 0

        # merge two parts in the right order
        while (i <= mid) and (j <= right):
            #if self.array[i] <= self.array[j]:
            if not self.more(i, j):
                temp_array[x] = self.array[i]
                self.asg += 1
                i += 1
                x += 1
            else:
                temp_array[x] = self.array[j]
                self.asg += 1
                j += 1
                x += 1
        while i <= mid:
            temp_array[x] = self.array[i]
            self.asg += 1
            i += 1
            x += 1
        while j <= right:
            temp_array[x] = self.array[j]
            self.asg += 1
            j += 1
            x += 1

        # copy sorted temp_array back to self.array in the right place
        for k in range(left, right + 1):
            self.asg += 1
            self.array[k] = temp_array[k - left]
        del temp_array

    def sort(self, left, right):
        if left >= right:
            return

        mid = int((left + right) / 2)
        self.sort(left, mid)
        self.sort(mid + 1, right)
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

    sort = MergeSort(create_array(100))
    start_time = time.time() * 1000.
    sort.sort(0, sort.N - 1)
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)
    print(sort.toString())