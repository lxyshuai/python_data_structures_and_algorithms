# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailNode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('FULL')
        node = Node(value)
        if self.tailNode is None:
            self.root.next = node
        else:
            self.tailNode.next = node
        self.tailNode = node
        self.length += 1

    def appendleft(self, value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailNode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        prevnode = self.root
        curnode = self.root.next
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailNode:
                    self.tailNode = prevnode
                del curnode
                self.length -= 1
                return 1  # 删除成功
            else:
                prevnode = curnode
        return -1  # 删除失败

    def find(self, value):
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):
        if self.root.next is None:
            raise Exception("pop from empty LinkedList")
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        self.length -= 1
        del headnode
        return value

    # 在value前插入new_value
    def insert(self, value, new_value):
        node = Node(new_value)
        if self.root.next.value == value:
            node.next = self.root.next
            self.root.next = node
        else:
            for curnode in self.iter_node():
                if curnode.next.value == value:
                    node.next = curnode.next
                    curnode.next = node
                    break

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    ll.clear()
    assert len(ll) == 0


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(3)
    ll.insert(4, 3)
    print(list(ll))


if __name__ == '__main__':
    test_linked_list_remove()
