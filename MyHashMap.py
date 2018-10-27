from Entry import Entry
from LinkedList import EntryLinkedList, EntryNode

DEFAULT_MAXIMUM_LOAD_FACTOR = 0.75
DEFAULT_MAXIMUM_UNLOAD_FACTOR = 0.25
MAXIMUM_CAPACITY = 1 << 30


class MyHashMap(object):
    DEFAULT_INITIAL_CAPACITY = 4

    def __init__(self, capacity=DEFAULT_INITIAL_CAPACITY, loadFactor=DEFAULT_MAXIMUM_LOAD_FACTOR):

        if capacity > MAXIMUM_CAPACITY:
            self.capacity = MAXIMUM_CAPACITY

        else:
            self.capacity = self.trim_power_of2(capacity)

        self.thresholdLoadFactor = DEFAULT_MAXIMUM_UNLOAD_FACTOR
        self.thresholdUnoadFactor = 0.
        self.size = 0
        self.table = [EntryLinkedList()] * capacity

    def trim_power_of2(self, initial_capacity):  # trims the capacity to power of 2
        capacity = 1
        while capacity < initial_capacity:
            capacity <<= 1

        return capacity

    def hash_code(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.capacity

    def clear(self):
        self.size = 0
        self.remove_entries()

    def remove_entries(self):
        for entry in self.table:
            if entry is not None:
                entry = None

    def contains_key(self, key):
        index = self.hash_code(key)
        if self.table[index].head is not None:
            return True
        return False

    def contains_value(self, value):
        for entry in self.table:
            if entry is not None:
                    last_entry = self.table[index].head
                    while last_entry is not None:
                        last_entry = last_entry.next
                        if last_entry.get_val() == value:
                            return True
        return False

    def get(self, key):  # returning an element by specified key
        if key is not None:
            index = self.hash_code(key)
            if self.table is not None:
                if self.table[index].head is not None:
                    last_entry = self.table[index].head
                    while last_entry is not None:
                        last_entry = last_entry.next
                        if last_entry.key == key:
                            return last_entry
        return None

    def put(self, key, value):  # adding an element to the map by specified key
        index = self.hash_code(key)
        if (self.get(key) is not None) & (self.table[index].head is not None):  # if the key already exists
            last_entry = self.table[index].head
            while last_entry is not None:
                last_entry = last_entry.next
                if last_entry.key == key:
                    oldValue = last_entry.get_val()
                    last_entry.set_val(value)
                    return oldValue

        if (self.size + 1 >= self.capacity * self.thresholdLoadFactor) | (self.get(key) is not None):  # if need rehash
            if self.capacity == MAXIMUM_CAPACITY:
                RuntimeError("Exceeding maximum capacity")
            # self.resize()

   #  if index is taken we make a linked list
        new_index = self.hash_code(key)
        last_entry = self.table[new_index].head
        while last_entry is not None:
            last_entry = last_entry.next
        last_entry = EntryNode(Entry(key, value))
        self.size = + 1
        return None

    # def resize(self):
    #     if self.size / self.capacity > self.thresholdLoadFactor:
    #         self.capacity = self.capacity * 2
    #         self.thresholdLoadFactor = self.capacity * 0.75
    #
    #     if self.size / self.capacity < self.thresholdUnoadFactor:
    #         self.capacity = self.capacity / 2
    #         self.thresholdLoadFactor = self.capacity * 0.75
    #
    #     old_table = self.table
    #     self.table = [None] * self.capacity
    #     for entry in old_table:
    #         if entry is not None:
    #             self.put(entry.get_key(), entry.get_val())

    def entry_set(self):  # return set of the entries(BandEntries) in the map
        h_set = set()
        for entry in self.table:
            if entry is not None:
                h_set.add(entry)
        return h_set

    def is_empty(self):  # returning if the map contains values or not
        return self.size == 0

    def key_set(self):  # returning a set of the keys in this map
        k_set = set()
        for entry in self.entry_set():
            k_set.add(entry.get_key())
        return k_set

    # def map_copy(self, map):  # adding a full map to this map
    #     m_set = map.entry_set()
    #
    #     for entry in m_set:
    #         self.put(entry.get_key(), entry.get_val())

    def remove(self, key):  # removing element by specified key
        if self.get(key) is None:
            return None

        index = self.hash_code(key)
        oldValue = self.table[index].get_val()
        self.table[index] = None
        self.size -= 1

        if self.size + 1 <= self.capacity * self.thresholdUnoadFactor:
            self.resize()

        return oldValue

    def value_set(self):  # return a set consisting of the values in the map
        v_list = list()
        for entry in self.entry_set():
            v_list.append(entry.get_val())
        return v_list

    def __str__(self):
        return str([str(entry) for entry in self.table if entry is not None])

    def generator(self):
        for index in range(-1, len(self.table) - 1, 1):
            yield self.table[index]


