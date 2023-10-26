"""
    你有一个包含 n 个节点的图。给定一个整数 n 和一个数组 edges ，其中 edges[i] = [ai, bi] 表示图中 ai 和 bi 之间有一条边。返回图中已连
接分量的数目 。

    示例 1:
        输入: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
        输出: 2


"""
from typing import List


class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.cnt = n

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        self.parent[root_x] = root_y
        self.cnt -= 1

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        return self.answer_1(n, edges)

    def answer_1(self, n, edges):
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)
        return uf.cnt
