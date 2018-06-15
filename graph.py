# -*- coding: utf-8 -*-

from collections import deque

GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


def bfs(graph, start):
    search_queue = Queue()
    search_queue.push(start)
    searched = set()
    while search_queue:
        cur = search_queue.pop()
        if cur not in searched:
            print cur
            searched.add(cur)
            for node in graph[cur]:
                search_queue.push(node)


def dfs(graph, start):
    DFS_SEARCHED = set()

    def dfs_recursion(graph, start):
        if start not in DFS_SEARCHED:
            print(start)
            DFS_SEARCHED.add(start)
        for node in graph[start]:
            if node not in DFS_SEARCHED:
                dfs_recursion(graph, node)

    dfs_recursion(graph, start)


bfs(GRAPH, 'A')
print('=====')
dfs(GRAPH, 'A')
