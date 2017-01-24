from basic_data_struct.hash_table.anagrams import find_anagrams


def test_find_anagrams():
    test = find_anagrams(['CAT', 'cat', 'caz', 'lumps', 'umpls'])

    assert [['CAT', 'cat'], ['lumps', 'umpls'], ['caz']] == list(test)

