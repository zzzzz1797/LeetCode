"""
    给你一棵二叉树，请按以下要求的顺序收集它的全部节点：
        依次从左到右，每次收集并删除所有的叶子节点
        重复如上过程直到整棵树为空

"""
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.answer_1(root)

    def answer_1(self, root):
        dic = collections.defaultdict(list)

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            d = max(left, right) + 1
            dic[d - 1].append(node.val)
            return d

        dep = dfs(root)

        return [dic[i] for i in range(dep)]
