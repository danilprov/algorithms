# https://leetcode.com/problems/implement-trie-prefix-tree/


class _Node:
    A = 128  # alphabet size

    def __init__(self):
        self.is_end = False # in this problem instead of value use indicator of finished word
        self.child = [None] * Node.A
        Trie.MEMORY += Node.A + 1

    def next(self, char):
        ichar = ord(char)
        if not self.exists(ichar):
            self.child[ichar] = Node()

        return self.child[ichar]

    def exists(self, ichar):
        return self.child[ichar] is not None


class Node:
    A = 128  # alphabet size

    def __init__(self):
        self.is_end = False # in this problem instead of value use indicator of finished word
        self.child = None
        Trie.MEMORY += 1

    def next(self, char):
        if self.child is None:
            self.child = [None] * Node.A
            Trie.MEMORY += Node.A
        ichar = ord(char)
        if not self.exists(ichar):
            self.child[ichar] = Node()

        return self.child[ichar]

    def exists(self, ichar):
        return self.child[ichar] is not None


class Trie:
    MEMORY = 0

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.next(char)
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.go(word)
        if node is None:
            return False
        else:
            return node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.go(prefix) is not None

    def go(self, word):
        node = self.root
        for char in word:
            ichar = ord(char)
            if node.exists(ichar):
                node = node.child[ichar]
            else:
                return None
        return node


if __name__ == '__main__':
    import random
    import string
    import time
    from HashTable import HashTable

    random.seed(123)
    def get_random_word():
        length = 10 #random.randint(3, 10)
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        #print("Random string of length", length, "is:", result_str)
        return result_str

    trie = Trie()
    hash = HashTable()
    n = 100000
    for i in range(n):
        word = get_random_word()
        trie.insert(word)
        hash.put(word, 0)

    print(trie.MEMORY)

    random.seed(123)
    count = 0
    start_time = time.time() * 1000.
    for i in range(n):
        if hash.constain_key(get_random_word()):
            count += 1
    print(f'Hash search found {count} elements; time - {round(time.time() * 1000. - start_time)} ms')

    random.seed(123)
    count = 0
    start_time = time.time() * 1000.
    for i in range(n):
        if trie.search(get_random_word()):
            count += 1
    print(f'Trie search found {count} elements; time - {round(time.time() * 1000. - start_time)} ms')

    print('a')