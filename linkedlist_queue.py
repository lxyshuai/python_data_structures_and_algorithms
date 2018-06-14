from linked_list import LinkedList


class FullError(Exception):

    pass


class EmptyError(Exception):
    pass


class LinkedListQueue(object):
    def __init__(self, maxsize=None):

        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        '''

        Returns:

        '''
        return len(self._item_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError("queue full")
        return self._item_linked_list.append(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError("queue empty")
        return self._item_linked_list.popleft()


def test_queue():
    queue = LinkedListQueue()
    queue.push(0)
    queue.push(1)
    queue.push(2)

    assert len(queue) == 3

    assert queue.pop() == 0
    assert queue.pop() == 1
    assert queue.pop() == 2

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        queue.pop()
    assert 'queue empty' == str(excinfo.value)