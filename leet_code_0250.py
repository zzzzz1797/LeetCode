"""
    给定一个二叉树，统计该二叉树数值相同的子树个数。同值子树是指该子树的所有节点都拥有相同的数值。

    示例1：
        输入: root = [5,1,5,5,5,null,5]
        输出: 4
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self._count = 0

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        return self.answer_1(root)

    def answer_1(self, root):
        self._dfs_1(root)
        return self._count

    def _dfs_1(self, node):
        flag = True
        if not node:
            return flag

        if not (node.left or node.right):
            self._count += 1
            return flag

        if node.left:
            flag = self._dfs_1(node.left) and node.left.val == node.val

        if node.right:
            flag = self._dfs_1(node.right) and flag and node.right.val == node.val

        if flag:
            self._count += 1
        return flag
