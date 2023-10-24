"""
    给定一棵 N 叉树 的所有节点在一个数组  Node[] tree 中，树中每个节点都有 唯一的值 。找到并返回 N 叉树的 根节点 。
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List[Node]) -> Node:
        return self.answer_1(tree)

    def answer_1(self, tree):
        value_sum = 0

        for node in tree:
            value_sum += node.val
            for child_node in node.children:
                value_sum -= child_node.val

        for node in tree:
            if value_sum == node.val:
                return node
