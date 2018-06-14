from double_link_list import CircualDoubleLinkedList


class Deque(CircualDoubleLinkedList):

    def pop(self):
        if len(self) == 0:
            raise Exception('empty')
        return self.remove(self.tailnode()).value

    def popleft(self):
        if len(self) == 0:
            raise Exception('empty')
        return self.remove(self.headnode()).value
