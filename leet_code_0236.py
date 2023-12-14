"""
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。百度百科中最近公共祖先的定义为：“对于有根树T的两个节点p、q，最近公共祖先表示为一个节
点x，满足x是p、q 的祖先且x的深度尽可能大（一个节点也可以是它自己的祖先）。”

    示例 1：
        输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        输出：3
        解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

    示例 2：
        输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
        输出：5
        解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

    示例 3：
        输入：root = [1,2], p = 1, q = 2
        输出：1
https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.answer_1(root, p, q)

    def answer_1(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.answer_1(root.left, p, q)
        right = self.answer_1(root.right, p, q)

        if not left:
            return right
        if not right:
            return left
        return root
