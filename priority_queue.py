from heap_sort import MaxHeap


class PriorityQueue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        entry = (priority, value)
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empyt(self):
        return len(self._maxheap) == 0


def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(1, '1')
    pq.push(5, '5')
    pq.push(2, '2')
    pq.push(3, '3')

    result = []
    while not pq.is_empyt():
        result.append(pq.pop())
    assert result == list(reversed(['1', '2', '3', '5']))