# http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                # while self.slots[nextslot] is not None and \
                while self.slots[nextslot] and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

#
# H = HashTable()
# H[54] = "cat"
# H[26] = "dog"
# H[93] = "lion"
# H[17] = "tiger"
# H[77] = "bird"
# H[31] = "cow"
# H[44] = "goat"
# H[55] = "pig"
# H[20] = "chicken"
# print(H.slots)
# [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]

# print(H.data)
# ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']


# class OrdTable(HashTable):
#     def ord_key(self, chars):
#         sum = 0
#         for char in chars:
#             sum += ord(char.lower())
#
#         print ("sum", sum)
#
#         return sum
#
#     def put(self, data):
#         super(OrdTable, self).put(self.ord_key(data))
#
#     def __setitem__(self, key, data):
#         self.put(self.ord_key(data), data)
#
#
# O = OrdTable()
# O.put("dog")
# O.put("dog")
# O.put("dog")
# O.put("lion")
# O.put("chicken")
#
# print(O.data)
# # [None, None, None, None, None, 'lion', 'dog', None, None, None, 'chicken']
#
# # better for anagrams would be use dict with lists as values


class OrdListHashTable(HashTable):

    @staticmethod
    def ord_key(chars):
        sum = 0
        for char in chars:
            sum += ord(char.lower())
        return sum

    def put(self, word, **kwargs):
        hash_code = self.ord_key(word)

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
    def __init__(self):
        self.data = {}

    @staticmethod
    def ord_key(chars):
        ord_sum = 0
        for char in chars:
            ord_sum += ord(char.lower())
        return ord_sum

    def add(self, word):
        # print(self.data[12] = '12')
        key = self.ord_key(word)
        if key in self.data:
            self.data[key].append(word)
        else:
            self.data[key] = [word]

    def get_all(self):
        return self.data.values()

# T = HashTableDict()
# T.add('CAT')
# T.add('act')
# print(T.data)
# {312: ['CAT', 'act']}
# print(T.get_all())
# dict_values([['CAT', 'act']])
