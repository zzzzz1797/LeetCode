"""
    给你一棵指定的二叉树的根节点 root ，请你计算其中 最长连续序列路径 的长度。
    最长连续序列路径 是依次递增 1 的路径。该路径，可以是从某个初始节点到树中任意节点，通过「父 - 子」关系连接而产生的任意路径。且必须从父节点
到子节点，反过来是不可以的。
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._max_length = 0

    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        return self.answer_1(root)

    def answer_1(self, root):
        self._dfs_1(root, None, 0)
        return self._max_length

    def _dfs_1(self, node, parent, length):
        if not node:
            return

        if parent and parent.val + 1 == node.val:
            length += 1
        else:
            length = 1

        self._max_length = max(self._max_length, length)
        self._dfs_1(node.left, node, length)
        self._dfs_1(node.right, node, length)

    def answer_2(self, root):
        self._dfs_2(root)
        return self._max_length

    def _dfs_2(self, node):
        if not node:
            return 0

        left = self._dfs_2(node.left) + 1
        right = self._dfs_2(node.right) + 1

        if node.left and node.left.val - 1 != node.val:
            left = 1
        if node.right and node.right.val - 1 != node.val:
            right = 1

        length = max(left, right)
        self._max_length = max(self._max_length, length)
        return length
