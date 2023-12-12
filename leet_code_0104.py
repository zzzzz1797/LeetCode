"""
    给定一个二叉树 root，返回其最大深度。二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

    示例 1：
        输入：root = [3,9,20,null,null,15,7]
        输出：3

    示例 2：
        输入：root = [1,null,2]
        输出：2

https://leetcode.cn/problems/maximum-depth-of-binary-tree/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.answer_1(root)

    def answer_1(self, root):
        def _dfs(node, result=0):
            if not node:
                return result
            left_high = _dfs(node.left)
            right_high = _dfs(node.right)
            return max(left_high, right_high) + 1

        return _dfs(root)

    def answer_2(self, root):
        depth = 0

        if not root:
            return depth

        stack = [(root, 1)]

        while stack:
            node, tmp_depth = stack.pop()

            if not node:
                continue

            depth = max(depth, tmp_depth)
            stack.append((node.left, tmp_depth + 1))
            stack.append((node.right, tmp_depth + 1))

        return depth
