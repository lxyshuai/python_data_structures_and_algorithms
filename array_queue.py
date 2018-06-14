from array_and_list import Array


class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('queue full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        if len(self) == 0:
            raise EmptyError('queue empty')
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value


def test_array_queue():
    import pytest
    size = 5
    queue = ArrayQueue(5)
    for i in range(size):
        queue.push(i)

    with pytest.raises(FullError) as excinfo:
        queue.push(size)
    assert 'queue full' == str(excinfo.value)

    assert len(queue) == size

    assert queue.pop() == 0
    assert queue.pop() == 1

    queue.push(5)
    assert len(queue) == 4

    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5

    assert len(queue) == 0
