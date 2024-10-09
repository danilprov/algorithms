class _HashEntry:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    DEFAULT_CAPASITY = 11
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self, initial_capacity = None, load_factor=None):
        self.size = 0
        if initial_capacity == 0:
            initial_capacity = 1
        self.capacity = initial_capacity if initial_capacity else HashTable.DEFAULT_CAPASITY
        self.buckets = [None for _ in range(self.capacity)]

        self.load_factor = load_factor if load_factor else HashTable.DEFAULT_LOAD_FACTOR
        self.threshold = int(self.load_factor * self.capacity)

    def get_size(self):
        return self.size

    def hash(self, key):
        hash = key.__hash__() % len(self.buckets)
        return hash if hash > 0 else -hash

    def rehash(self):
        old_buckets = self.buckets
        self.capacity = self.capacity * 2 + 1
        self.threshold = int(self.load_factor * self.capacity)

        self.buckets = [None for _ in range(self.capacity)]
        for i in range(len(old_buckets)):
            current_bucket = old_buckets[i]
            while current_bucket:
                idx = self.hash(current_bucket.key)
                dest = self.buckets[idx]
                if dest:
                    next_node = dest.next
                    while next_node:
                        dest = next_node
                        next_node = dest.next
                    dest.next = current_bucket
                else:
                    self.buckets[idx] = current_bucket

                next_node = current_bucket.next
                current_bucket.next = None
                current_bucket = next_node

    def contains(self, value):
        assert value is not None, ValueError("value cannot be None")

        for i in range(self.capacity):
            current_bucket = self.buckets[i]
            while current_bucket:
                if current_bucket.value == value:
                    return True
                current_bucket = current_bucket.next

        return False

    def contains_key(self, key):
        idx = self.hash(key)
        target_bucket = self.buckets[idx]
        while target_bucket:
            if target_bucket.key == key:
                return True
            target_bucket = target_bucket.next

        return False

    def get(self, key):
        idx = self.hash(key)
        target_bucket = self.buckets[idx]
        while target_bucket:
            if target_bucket.key == key:
                return target_bucket.value
            target_bucket = target_bucket.next

        return None

    def put(self, key, value):
        assert value is not None, ValueError("value cannot be None")
        idx = self.hash(key)
        target_bucket = self.buckets[idx]

        while target_bucket:
            if target_bucket.key == key:
                old_value = target_bucket.value
                target_bucket.value = value
                return old_value
            target_bucket = target_bucket.next

        self.size += 1
        if self.size > self.threshold:
            self.rehash()
            idx = self.hash(key)

        new_bucket = _HashEntry(key, value)
        new_bucket.next = self.buckets[idx]
        self.buckets[idx] = new_bucket

    def remove(self, key):
        idx = self.hash(key)
        target_bucket = self.buckets[idx]
        last_node = None

        while target_bucket:
            if target_bucket.key == key:
                if last_node:
                    last_node.next = target_bucket.next
                else:
                    self.buckets[idx] = target_bucket.next
                self.size -= 1
                return target_bucket.value

            last_node = target_bucket
            target_bucket = target_bucket.next

        return None
