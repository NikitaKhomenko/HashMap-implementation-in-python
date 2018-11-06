from MyHashMap import MyHashMap


def main():

    print('Hello, this is my hash map example.\n')

    map1 = MyHashMap()

    map1.put(1953, 'Subaru')
    map1.put(1970, 'Mitsubishi')
    map1.put(1899, 'Fiat')
    map1.put(1916, 'BMW')

    set1 = map1.entry_set()
    print(set1)

    print('Map 1:\n')
    map1.print_map()

    map2 = MyHashMap()

    print('Copping map 1 to map 2:\n')
    # map2.map_copy(map1)

    print('Map 2:\n')
    map2.print_map()


main()
