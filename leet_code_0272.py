"""
    给定二叉搜索树的根 root 、一个目标值 target 和一个整数 k ，返回BST中最接近目标的 k 个值。你可以按 任意顺序 返回答案。题目保证该二叉搜索
树中只会存在一种 k 个值集合最接近 target。

    示例 1：
        输入: root = [4,2,5,1,3]，目标值 = 3.714286，且 k = 2
        输出: [4,3]

    示例 2:
        输入: root = [1], target = 0.000000, k = 1
        输出: [1]

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        return self.answer_1(root, target, k)

    def answer_1(self, root, target, k):
        smaller_stack, larger_stack = [], []

        while root:
            if root.val < target:
                smaller_stack.append(root)
                root = root.right
            else:
                larger_stack.append(root)
                root = root.left

        result = []

        for index in range(k):
            left_diff = float("inf") if not smaller_stack else target - smaller_stack[0].val
            right_diff = float("inf") if not larger_stack else larger_stack[0].val - target

            if left_diff <= right_diff:
                node = smaller_stack.pop()
                result.append(node.val)
                node = node.left
                while node:
                    smaller_stack.append(node)
                    node = node.right
            else:
                node = larger_stack.pop()
                result.append(node.val)
                node = node.right
                while node:
                    larger_stack.append(node)
                    node = node.left
        return result
