"""
    给你一个二叉树的根结点，返回其结点按 垂直方向（从上到下，逐列）遍历的结果。如果两个结点在同一行和列，那么顺序则为 从左到右。

    示例 1：
        输入：root = [3,9,20,null,null,15,7]
        输出：[[9],[3,15],[20],[7]]

    示例 2：
        输入：root = [3,9,8,4,0,1,7]
        输出：[[4],[9],[3,0,1],[8],[7]]
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
