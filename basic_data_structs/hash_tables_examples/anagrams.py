from basic_data_structs.dictionary import HashTableDict


# f O(N L log L)
def find_anagrams(words):
    hash_dict = HashTableDict()

    for word in words:
        hash_dict.add(word)

    return hash_dict.get_all()
