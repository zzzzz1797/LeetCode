"""
    给你一个二叉树的根结点，返回其结点按 垂直方向（从上到下，逐列）遍历的结果。如果两个结点在同一行和列，那么顺序则为 从左到右。

    示例 1：
        输入：root = [3,9,20,null,null,15,7]
        输出：[[9],[3,15],[20],[7]]

    示例 2：
        输入：root = [3,9,8,4,0,1,7]
        输出：[[4],[9],[3,0,1],[8],[7]]
"""
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.answer_1(root)

    def answer_1(self, root):
        table = collections.defaultdict(list)

        queue = collections.deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if not node:
                continue

            table[column].append(node.val)
            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))

        return [table[i] for i in sorted(table)]
