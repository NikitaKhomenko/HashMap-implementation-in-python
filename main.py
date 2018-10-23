from MyHashMap import MyHashMap


def main():
    print('Hello, this is my hash map example.\n')

    map1 = MyHashMap()

    map1.put(1, 'nikita')
    map1.put(2, 'shimon')
    map1.put(3, 'linoy')
    map1.put(4, 'moshe')

    print('Map 1:\n')
    map1.__str__()

    map2 = MyHashMap()

    print('Copping map 1 to map 2:\n')
    map2.putAll(map1)

    print('Map 2:\n')
    map2.__str__()


main()
