from basic_data_struct.dictionary import OrdTable, HashTableDict, OrdListHashTable
from basic_data_struct.hash_table import HashTable


def test_ord_table():
    o = OrdTable()
    o.put("dog")
    o.put("dog")
    o.put("dog")
    o.put("lion")
    o.put("chicken")

    print(o.data)
    # [None, None, None, None, None, 'lion', 'dog', None, None, None, 'chicken']

    assert 'lion' in o.data
    assert 'dog' in o.data
    assert 'lion' in o.data
    assert 'chicken' in o.data


def test_ord_hash_table():
    ord_list = OrdListHashTable()
    ord_list.put('doge')
    ord_list.put('dgeo')
    ord_list.put('oged')
    ord_list.put('Cat')
    ord_list.put('cat')

    print(ord_list.data)
    # [None, None, None, None, ['Cat', 'cat', 'cat'], None, None, None, ['doge', 'dgeo', 'dgeo', 'oged', 'oged'],
    # None, None]


def test_hash_table_with_dict():
    t = HashTableDict()
    t.add('CATS')
    t.add('acts')
    t.add('else')

    print(t.data)
    # {312: ['CAT', 'act']}
    print(t.get_all())
    # dict_values([['CAT', 'act']])
    assert list(t.get_all()) == [['else'], ['CATS', 'acts']]


def test_hash_table():
    h = HashTable()
    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion"
    h[17] = "tiger"
    h[77] = "bird"
    h[31] = "cow"
    h[44] = "goat"
    h[55] = "pig"
    h[20] = "chicken"
    print(h.slots)
    # [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]

    # print(H.data)
    # ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
