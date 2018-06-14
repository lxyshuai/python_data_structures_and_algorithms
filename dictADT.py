from hashtable import HashTable


class DictADT(HashTable):

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            return self.get(key)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def item(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value

def test_dict_adt():
    import random
    dict = DictADT()

    dict['a'] = 1
    assert dict['a'] == 1
    dict.remove('a')

    l = list(range(30))
    random.shuffle(l)
    for i in l:
        dict.add(i,i)

    for i in l:
        assert dict[i] == i
