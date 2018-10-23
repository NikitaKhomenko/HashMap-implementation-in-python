from MyHashMap import MyHashMap


def main():
    print('Hello, this is my hash map example.\n')

    map1 = MyHashMap()

    map1.Put(1953, 'Subaru')
    map1.Put(1970, 'Mitsubishi')
    map1.Put(1899, 'Fiat')
    map1.Put(1916, 'BMW')

    print('Map 1:\n')
    map1.__str__()

    map2 = MyHashMap()

    print('Copping map 1 to map 2:\n')
    map2.PutAll(map1)

    print('Map 2:\n')
    map2.__str__()


main()
