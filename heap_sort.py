from array_and_list import Array


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._siftup(self._count)
        self._count += 1

    def _siftup(self, index):
        if index <= 0:
            return

        parent = int((index - 1) / 2)
        if self._elements[index] > self._elements[parent]:
            self._elements[index], self._elements[parent] = self._elements[parent], self._elements[index]
            self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < self._count and self._elements[left] >= self._elements[largest]:
            largest = left
        if right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != index:
            self._elements[index], self._elements[largest] = self._elements[largest], self._elements[index]
            self._siftdown(largest)


def heap_sort(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for x in array:
        maxheap.add(x)
    result = []
    for x in range(length):
        result.append(maxheap.extract())
    return result


def test_max_heap():
    import random
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert h.extract() == i


def test_heap_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq, reverse=True)
    seq = heap_sort(seq)
    assert seq == sorted_seq
