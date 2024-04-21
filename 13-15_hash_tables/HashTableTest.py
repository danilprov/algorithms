import unittest
from HashTable import HashTable

class HashTableTest(unittest.TestCase):
    def test_put_get(self):
        hash_table = HashTable()
        hash_table.put("key1", 0)
        hash_table.put("key2", 1)

        self.assertEqual(hash_table.get("key1"), 0)
        self.assertEqual(hash_table.get("key2"), 1)
        self.assertFalse(hash_table.get("key3"))

    def test_contains(self):
        hash_table = HashTable()
        hash_table.put("key1", "value1")

        self.assertTrue(hash_table.contains("value1"))
        self.assertFalse(hash_table.contains("value2"))

    def test_contains_key(self):
        hash_table = HashTable()
        hash_table.put("key1", "value1")

        self.assertTrue(hash_table.contains_key("key1"))
        self.assertFalse(hash_table.contains_key("key2"))

    def test_remove(self):
        hash_table = HashTable()
        hash_table.put("key1", "value1")
        hash_table.put("key2", "value2")
        hash_table.remove("key1")

        self.assertFalse(hash_table.contains("value1"))
        self.assertTrue(hash_table.contains("value2"))


if __name__ == '__main__':
    unittest.main()
