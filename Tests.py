import unittest
from MyHashMap import MyHashMap

map1 = MyHashMap()
map1.put(1953, 'Subaru')
map1.put(1970, 'Mitsubishi')
map1.put(1899, 'Fiat')
map1.put(1916, 'BMW')

map2 = MyHashMap()
map2.map_copy(map1)

entry = map1.get(1953)


class TestHashCode(unittest.TestCase):

    def test_get(self):
        self.assertIs(entry.get_val(), 'Subaru')

    def test_hash_code(self):
        self.assertEqual(map1.hash_code(entry.get_key()), 2)

    def test_contains_value(self):
        self.assertTrue(map1.contains_value(entry.get_val()))
        self.assertFalse(map1.contains_value('something'))

    def test_contains_key(self):
        self.assertTrue(entry.get_key())

    def test_trim_power_of2(self):
        self.assertEqual(map1.trim_power_of2(15), 16)

    def test_entry_set(self):
        entry_set1 = map1.entry_set()
        self.assertIn(entry, entry_set1)

    def test_key_set(self):
        key_set1 = map1.key_set()
        self.assertIn(1953, key_set1)

    def test_value_set(self):
        value_set1 = map1.value_set()
        self.assertIn('Fiat', value_set1)

    def test_remove(self):
        self.assertIs(map1.remove(1916), 'BMW')

    def test_resize(self):
        map1.resize()
        self.assertEqual(map1.capacity, 4)

    def test_put(self):
        old_val = map2.put(1899, 'Toyota')
        self.assertIs(old_val, 'Fiat')






