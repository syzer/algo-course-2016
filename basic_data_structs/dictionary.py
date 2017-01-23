from basic_data_structs.hash_table import HashTable


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

    def put(self, word, **kwargs):
        hash_code = ord_key(word)

        if self.get(hash_code) is None:
            super().put(hash_code, [word])
        else:
            prev = self.get(hash_code)
            prev.append(word)
            super().put(hash_code, prev)

# [None, None, None, None, ['Cat', 'cat', 'cat'], None, None, None, ['doge', 'dgeo', 'dgeo', 'oged', 'oged'], None, None]


# Dict = OrdListHashTable()
# Dict.put('doge')
# Dict.put('dgeo')
# Dict.put('oged')
# Dict.put('Cat')
# Dict.put('cat')

# assert Dict.get('dog')
# assert Dict.get('oge')
# assert Dict.get('cat')
# print(Dict.data)


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
