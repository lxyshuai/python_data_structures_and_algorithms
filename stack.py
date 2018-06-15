from deque import Deque



class Stack():
    def __init__(self):
        self.deque = Deque()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


def test_stack():
    stack = Stack()
    for i in range(3):
        stack.push(i)

    assert len(stack) == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == 0

    assert stack.is_empty()

    import pytest
    with pytest.raises(Exception) as excinfo:
        stack.pop()
    assert 'empty' in str(excinfo)
