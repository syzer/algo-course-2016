from hash_table import HashTableDict


# f O(N L log L)
def find_anagrams(words):
    hash_dict = HashTableDict()

    for word in words:
        hash_dict.add(word)

    return hash_dict.get_all()

test = find_anagrams(['CAT', 'cat', 'caz', 'lumps', 'umpls'])
# dict_values([['CAT', 'cat'], ['lumps', 'umpls'], ['caz']])

print(test)