import unittest
from MyHashMap import MyHashMap
from Entry import Entry


class TestHashCode(unittest.TestCase):
    def test_hash_code(self):
        map1 = MyHashMap()
        entry1 = Entry(1953, 'Subaru')
        map1.put(entry1.get_key(), entry1.get_val())
        self.assertEqual(map1.hash_code(entry1.get_key()), 2)


