# -*- coding: utf-8 -*-


class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """build_from
        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)

    def preorder_trav_recursion(self, subtree):
        if subtree is None:
            return

        print subtree.data
        self.preorder_trav_recursion(subtree.left)
        self.preorder_trav_recursion(subtree.right)

    def preorder_trav_nonrecursion(self, subtree):
        if (subtree):
            myStack = []
            myStack.append(subtree)
            while myStack:
                subtree = myStack.pop()
                print subtree.data
                if subtree.right:
                    myStack.append(subtree.right)
                if subtree.left:
                    myStack.append(subtree.left)

    def postorder_trav_recursion(self, subtree):
        if subtree is None:
            return

        self.postorder_trav_recursion(subtree.left)
        self.postorder_trav_recursion(subtree.right)
        print subtree.data

    def postorder_trav_nonrecursion(self, subtree):
        if subtree:
            myStack = []
            helpStack = []
            myStack.append(subtree)
            while myStack:
                subtree = myStack.pop()
                helpStack.append(subtree)
                if subtree.left:
                    myStack.append(subtree.left)
                if subtree.right:
                    myStack.append(subtree.right)

            while helpStack:
                print helpStack.pop().data

    def inorder_trav_recursion(self, subtree):
        if subtree is None:
            return

        self.inorder_trav_recursion(subtree.left)
        print subtree.data
        self.inorder_trav_recursion(subtree.right)

    def inorder_trav_nonrecursion(self, subtree):
        if subtree:
            myStack = []
            while myStack or subtree:
                if subtree:
                    myStack.append(subtree)
                    subtree = subtree.left
                else:
                    subtree = myStack.pop()
                    print subtree.data
                    subtree = subtree.right


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

if __name__ == '__main__':
    btree = BinTree.build_from(node_list)
    btree.preorder_trav_recursion(btree.root)
    print '===='
    btree.preorder_trav_nonrecursion(btree.root)
    print '===='
    btree.postorder_trav_recursion(btree.root)
    print '===='
    btree.postorder_trav_nonrecursion(btree.root)
    print '===='
    btree.inorder_trav_recursion(btree.root)
    print '===='
    btree.inorder_trav_nonrecursion(btree.root)
