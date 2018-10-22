class MyHashMap():
    DEFAULT_INITIAL_CAPACITY = 4
    DEFAULT_MAXIMUM_LOAD_FACTOR = 0.75
    MAXIMUM_CAPACITY = 1 << 30

    def __init__(self, capacity=DEFAULT_INITIAL_CAPACITY, loadFactor=DEFAULT_MAXIMUM_LOAD_FACTOR):

        if capacity > self.MAXIMUM_CAPACITY:
            self.capacity = self.MAXIMUM_CAPACITY

        else:
            self.capacity = self.trimToPowerOf2(capacity)

        self.thresholdLoadFactor = loadFactor
        self.size = 0
        self.table = [None] * capacity

    class Entry:
        def __init__(self, key, val):
            self.key = key
            self.val = val

            def getKey(self):
                return self.key

            def getVal(self):
                return self.val

            def setVal(self, val):
                self.val = val

            def __str__(self):
                return "(" + self.key + ": " + str(self.val) + ")"

    def hashCode(self, data):
        h = 0
        for c in data:
            h = (31 * h + ord(c)) & 0xFFFFFFFF
        return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

    def trimToPowerOf2(self, initialCapacity):  # trims the capacity to power of 2
        capacity = 1
        while capacity < initialCapacity:
            capacity <<= 1

        return capacity

    def hashIt(self, hashCode):
        return self.supplyHashCode(hashCode) & (self.capacity - 1)

    def supplyHashCode(self, h):
        h ^= (h >> 20) ^ (h >> 12)
        return h ^ (h >> 7) ^ (h >> 4)

    def clear(self):
        self.size = 0
        self.removeEntries()

    def removeEntries(self):
        for entry in self.table:
            if entry is not None:
                entry = None

    def containsKey(self, key):
        index = self.hashIt(key)
        if (self.table[index] is not None) & (self.table[index].getKey().equals(key)):
            return True
        return False

    def containsValue(self, value):
        for entry in self.table:
            if entry is not None:
                if entry.getValue().equals(value):
                    return True
        return False

    def put(self, key, value):  # adding an element to the map by specified key
        index = self.hashIt(key)
        if (self.get(key) is not None) & (self.table[index].getKey().equals(key)):  # if the key already exists
            oldValue = self.table[index].getValue()
            self.table[index].setValue(value)
            return oldValue

        if (self.size + 1 >= self.capacity * self.thresholdLoadFactor) | (self.get(key) is not None):  # if need rehash
            if self.capacity == self.MAXIMUM_CAPACITY:
                RuntimeError("Exceeding maximum capacity")
            self.rehash()

        newIndex = self.hashIt(key)
        self.table[newIndex] = self.Entry(key, value)
        self.size = + 1
        return None

    def rehash(self):  # the rehash function
        h_set = self.entrySet()
        self.capacity <<= 1
        self.table = self.Entry[self.capacity]
        self.size = 0
        for entry in h_set:
            self.put(entry.getKey(), entry.getValue())

    def entrySet(self):  # return set of the entries(BandEntries) in the map
        h_set = set()
        for entry in self.table:
            if entry is not None:
                h_set.add(entry)
        return h_set

    def get(self, key):  # returning an element by specified key
        if key is not None:
            index = self.hashIt(key)
            if self.table is not None:
                return self.table[index].getValue()
        return None

    def isEmpty(self):  # returning if the map contains values or not
        return self.size == 0

    def keySet(self):  # returning a set of the keys in this map
        k_set = set()
        for entry in self.entrySet():
            k_set.add(entry.getKey())
        return k_set

    def putAll(self, map):  # adding a full map to this map
        m_set = map.entrySet()

        for self.entry in m_set:
            self.put(self.entry.getKey(), self.entry.getValue())

    def remove(self, key):  # removing element by specified key
        if self.get(key) is None:
            return None

        index = self.hashIt(key)
        oldValue = self.table[index].getValue()
        self.table[index] = None
        self.size -= 1
        return oldValue

    def size(self):  # retutn size of the map
        return self.size

    def values(self):  # return a set consisting of the values in the map
        v_list = list()
        for entry in self.entrySet():
            v_list.append(entry.getValue())
        return list

    def __call__(self):
        return self.__init__()

    def __str__(self):
        return str(self.table)


def main():
    print('hello')

    map1 = MyHashMap(16)

    map1.put(1, 'nikita')
    map1.put(2, 'shimon')
    map1.put(3, 'linoy')
    map1.put(4, 'moshe')

    map2 = MyHashMap()

    map2.putAll(map1)
    print('hello')
    map2.__str__()


main()
