"""
    给出两棵二叉搜索树的根节点root1和root2，请你从两棵树中各找出一个节点，使得这两个节点的值之和等于目标值 Target。如果可以找到返回True，否
则返回 False。

    示例 1：
        输入：root1 = [2,1,4], root2 = [1,0,3], target = 5
        输出：true
        解释：2 加 3 和为 5 。

    示例 2：
        输入：root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
        输出：false
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        return self.answer_1(root1, root2, target)

    def answer_1(self, root1, root2, target):
        values1 = self._in_order(root1)
        values2 = self._in_order(root2)

        index1 = 0
        index2 = len(values2) - 1

        while index1 < len(values1) and index2 > 0:
            value1 = values1[index1]
            value2 = values2[index2]

            cmp_target = value1 + value2

            if cmp_target == target:
                return True
            elif cmp_target < target:
                index1 += 1
            elif cmp_target > target:
                index2 -= 1

        return False

    def _in_order(self, node, result=None):
        if result is None:
            result = []

        if not node:
            return result
        self._in_order(node.left, result)
        result.append(node.val)
        self._in_order(node.right, result)
        return result
