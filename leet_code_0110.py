"""
    给定一个二叉树，判断它是否是高度平衡的二叉树。

    本题中，一棵高度平衡二叉树定义为：
        一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

    示例 1：
        输入：root = [3,9,20,null,null,15,7]
        输出：true

    示例 2：
        输入：root = [1,2,2,3,3,null,null,4,4]
        输出：false

    示例 3：
        输入：root = []
        输出：true

https://leetcode.cn/problems/balanced-binary-tree/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.answer_1(root)

    def answer_1(self, root):
        if not root:
            return True
        left_high = self._get_tree_high(root.left)
        right_high = self._get_tree_high(root.right)
        return not abs(right_high - left_high) > 1 and self.answer_1(root.left) and self.answer_1(root.right)

    def _get_tree_high(self, node):
        if not node:
            return 0
        return max(self._get_tree_high(node.left), self._get_tree_high(node.right)) + 1
