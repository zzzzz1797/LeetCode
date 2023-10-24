"""
    给你一棵二叉树的根节点，返回该树的直径。二叉树的直径是指树中任意两个节点之间最长路径的长度。这条路径可能经过也可能不经过根节点root 。两节点
之间路径的长度由它们之间边数表示。

    示例 1：
        输入：root = [1,2,3,4,5]
        输出：3
        解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。


    示例 2：
        输入：root = [1,2]
        输出：1
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.answer_1(root)

    def answer_1(self, root):
        result = 1

        def _dfs(node):
            if not node:
                return 0
            left = _dfs(node.left)
            right = _dfs(node.right)

            nonlocal result
            result = max(result, left + right + 1)
            return max(left, right) + 1

        _dfs(root)

        return result - 1
