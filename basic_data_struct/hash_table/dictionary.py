from basic_data_struct.manually_implemented import HashTable


class OrdTable(HashTable):

    def put(self, data):
        super().put(ord_key(data), data)

    def __setitem__(self, key, data):
        self.put(data)


def ord_key(chars):
    ord_sum = 0
    for char in chars:
        ord_sum += ord(char.lower())

    return ord_sum


class OrdListHashTable(HashTable):
    """
    better for anagrams would be use dict with lists as values
    """

    def put(self, word):
        hash_code = ord_key(word)

        if self.get(hash_code) is None:
            super().put(hash_code, [word])
        else:
            prev = self.get(hash_code)
            prev.append(word)
            super().put(hash_code, prev)


class HashTableDict:
    """
    hash table using dict
    """
    def __init__(self):
        self.data = {}

    def add(self, word):
        key = ord_key(word)
        if key in self.data:
            self.data[key].append(word)
        else:
            self.data[key] = [word]

    def get_all(self):
        return self.data.values()
