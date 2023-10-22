"""
    给你二叉搜索树的根节点 root 和一个目标值 target ，请在该二叉搜索树中找到最接近目标值 target 的数值。如果有多个答案，返回最小的那个。
    示例 1：
        输入：root = [4,2,5,1,3], target = 3.714286
        输出：4

    示例 2：
        输入：root = [1], target = 4.428571
        输出：1

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self._diff = float("inf")
        self._result = float("inf")

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self._dfs_1(root, target)
        return self._result

    def _dfs_1(self, root, target):
        if not root:
            return

        val = root.val
        diff = abs(val - target)

        if self._diff > diff:
            self._diff = diff
            self._result = val

        if self._diff == diff:
            self._result = min(self._result, val)

        if val < target:
            self._dfs_1(root.right, target)

        if val > target:
            self._dfs_1(root.left, target)
