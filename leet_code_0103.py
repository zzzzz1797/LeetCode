"""
    给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

    示例 1：
        输入：root = [3,9,20,null,null,15,7]
        输出：[[3],[20,9],[15,7]]

    示例 2：
        输入：root = [1]
        输出：[[1]]

    示例 3：
        输入：root = []
        输出：[]
https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.answer_1(root)

    def answer_1(self, root):
        result = []

        queue = [root]

        index = 0

        while queue:
            tmp_queue = []
            tmp_res = []

            for node in queue:
                if not node:
                    continue

                tmp_queue.append(node.left)
                tmp_queue.append(node.right)
                tmp_res.append(node.val)

            if index % 2 == 0:
                tmp_res.reverse()

            queue = tmp_queue
            if tmp_res:
                result.append(tmp_res)

            index += 1

        return result
