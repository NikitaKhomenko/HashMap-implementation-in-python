import MyHashMap


def main():
    print('hello')

    map1 = MyHashMap()

    map1.put(1, 'nikita')
    map1.put(2, 'shimon')
    map1.put(3, 'linoy')
    map1.put(4, 'moshe')

    map2 = MyHashMap()

    map2.putAll(map1)
    print('hello')
    map2.__str__()


main()
