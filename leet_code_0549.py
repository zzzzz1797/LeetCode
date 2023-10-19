"""
    给定二叉树的根 root ，返回树中最长连续路径的长度。
    连续路径是路径中相邻节点的值相差 1 的路径。此路径可以是增加或减少。
    例如， [1,2,3,4] 和 [4,3,2,1] 都被认为有效，但路径 [1,2,4,3] 无效。
    另一方面，路径可以是子-父-子顺序，不一定是父子顺序。

    示例 1:
        输入: root = [1,2,3]
        输出: 2
        解释: 最长的连续路径是 [1, 2] 或者 [2, 1]。

    示例 2:
        输入: root = [2,1,3]
        输出: 3
        解释: 最长的连续路径是 [1, 2, 3] 或者 [3, 2, 1]。

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
        """
        底层到当前节点最长的递增连续路径长度
        底层到当前节点最长的递减连续路径长度

        :param root:
        :return:
        """
        return self.answer_1(root)

    def answer_0(self, root):
        self._dfs_0(root)
        return self._max_length

    def _dfs_0(self, node):
        if not node:
            return 0, 0

        left_up, left_down = self._dfs_0(node.left)
        right_up, right_down = self._dfs_0(node.right)

        new_up = new_down = 1

        if node.left and node.left.val + 1 == node.val:
            new_up = max(new_up, left_up + 1)
        if node.left and node.left.val - 1 == node.val:
            new_down = max(new_down, left_down + 1)

        if node.right and node.right.val + 1 == node.val:
            new_up = max(new_up, right_up + 1)

        if node.right and node.right.val - 1 == node.val:
            new_down = max(new_down, right_down + 1)

        self._max_length = max(self._max_length, new_up + new_down - 1)
        return new_up, new_down

    def answer_1(self, root):
        self._dfs_1(root)
        return self._max_length

    def _dfs_1(self, node):
        if not node:
            return 0, 0
        left = self._dfs_1(node.left)
        right = self._dfs_1(node.right)

        inc = dec = 1
        if node.left:
            if node.left.val == node.val + 1:
                inc += left[0]
            elif node.left.val == node.val - 1:
                dec += left[1]

        if node.right:
            if node.right.val == node.val + 1:
                inc = max(inc, right[0] + 1)
            elif node.right.val == node.val - 1:
                dec = max(dec, right[1] + 1)
        self._max_length = max(self._max_length, dec + inc - 1)
        return inc, dec
