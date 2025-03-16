# Implemented with open addressing

class Pair:
    def __init__(self, key, val):
        # both key and val are strings
        self.key = key
        self.val = val


class HashMap:
    def __init__(self):
        self.size = 0  # number of keys in the hash map, initially 0
        self.capacity = 2
        self.map = [None, None]  # hash map is maintained as an array

    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

    def get(self, key):
        index = self.hash(key)

        while self.map[index] is not None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity  # to ensure we do not go out of bounds
        return None

    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] is None:  # if no key exists at the index, add the new key-value pair
                self.map[index] = Pair(key, val)
                self.size += 1
                # we divide capacity by 2 and then compare because we are taking load factor into consideration
                # I.e., we are checking if the hash map has been filled greater than 50%
                # If we remove // 2, we would only rehash once the hash map is completely filled
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:  # if the key is already in the map, update the value
                self.map[index].val = val
                return

            index += 1
            index = index % self.capacity

    def remove(self, key):
        # there is an implementation, but it is buggy so omitting this for now until I find something or code it myself
        pass

    def rehash(self):
        self.capacity = 2 * self.capacity  # naïve approach, not using prime numbers
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)

    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)
