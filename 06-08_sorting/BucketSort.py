from ISort import ISort


class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList():
    def __init__(self, first_node=None):
        self.length = 0
        self.head = first_node

    def add_correct_place(self, node):
        current_node = self.head
        while current_node.next and (node.value >= current_node.value) and (
                node.value < current_node.next.value):
            current_node = current_node.next

        node.next = current_node.next
        current_node.next = node

    def unpack_list(self):
        res = []
        current_node = self.head
        while current_node:
            res.append(current_node.value)
            current_node = current_node.next

        return res


class BucketSort(ISort):
    def __init__(self, array):
        super().__init__(array)
        self.bucket = None

    def sort(self, left, right):
        max_value = self.find_max()
        self.bucket = [LinkedList()] * self.N

        for i in range(self.N):
            idx = int(self.array[i] * self.N / (max_value + 1))
            node = Node(self.array[i])
            if self.bucket[idx].head is None:
                self.bucket[idx] = LinkedList(node)
            else:
                self.bucket[idx].add_correct_place(node)

        self.unpack_bucket()

    def unpack_bucket(self):
        sorted_array = []
        for linked_list in self.bucket:
            sorted_array += linked_list.unpack_list()

        self.array = sorted_array

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

    a = [5, 3, 7, 4, 2, 9, 1, 0, 6, 8]
    r = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    sort = BucketSort(create_array(100))
    start_time = time.time() * 1000.
    sort.sort(0, sort.N - 1)
    print(f'time spent - {round(time.time() * 1000. - start_time)} ms')
    print(sort.array)
    print(sort.toString())