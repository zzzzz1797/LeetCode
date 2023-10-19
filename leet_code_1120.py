"""
    给你一棵二叉树的根节点 root，找出这棵树的 每一棵 子树的 平均值 中的 最大 值。子树是树中的任意节点和它的所有后代构成的集合。树的平均值是树
中节点值的总和除以节点数。

    示例1：
        输入：[5,6,1]
        输出：6.00000
        解释：
            以 value = 5 的节点作为子树的根节点，得到的平均值为 (5 + 6 + 1) / 3 = 4。
            以 value = 6 的节点作为子树的根节点，得到的平均值为 6 / 1 = 6。
            以 value = 1 的节点作为子树的根节点，得到的平均值为 1 / 1 = 1。
            所以答案取最大值 6。
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._result = 0

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        return self.answer_1(root)

    def answer_1(self, root):
        self._dfs_1(root)
        return self._result

    def _dfs_1(self, node):
        if not node:
            return 0, 0

        left_sum, left_cnt = self._dfs_1(node.left)
        right_sum, right_cnt = self._dfs_1(node.right)

        current_sum = left_sum + right_sum + node.val
        current_cnt = left_cnt + right_cnt + 1

        avg_num = current_sum / current_cnt
        self._result = max(self._result, avg_num)
        return current_sum, current_cnt
