from hashtable import HashTable

class SetADT(HashTable):

    def add(self, key):
        return super(SetADT, self).add(key, True)

    def __and__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            if element_a in other_set:
                new_set.add(element_a)
        return new_set

    def __sub__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            if element_a not in other_set:
                new_set.add(element_a)
        return new_set

    def __or__(self, other_set):
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)
        for element_b in other_set:
            new_set.add(element_b)
        return new_set

def test_set_adt():
    setA = SetADT()
    setA.add(1)
    setA.add(2)
    setA.add(3)
    assert 1 in setA

    setB = SetADT()
    setB.add(3)
    setB.add(4)
    setB.add(5)
    assert 3 in setB

    assert sorted(list(setA & setB)) ==[3]
    assert sorted(list(setA - setB)) == [1, 2]
    assert sorted(list(setA | setB)) == [1, 2, 3, 4, 5]