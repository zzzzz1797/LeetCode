"""
    设计一个算法，可以将N叉树编码为二叉树，并能将该二叉树解码为原N叉树。一个 N 叉树是指每个节点都有不超过 N 个孩子节点的有根树。类似地，一个二
叉树是指每个节点都有不超过 2 个孩子节点的有根树。你的编码/解码的算法的实现没有限制，你只需要保证一个 N 叉树可以编码为二叉树且该二叉树可以解码回
原始N叉树即可。


    注意：
        N 的范围在 [1, 1000]
        不要使用类成员 / 全局变量 / 静态变量来存储状态。你的编码和解码算法应是无状态的。
https://leetcode.cn/problems/encode-n-ary-tree-to-binary-tree
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def encode(self, root: Node) -> TreeNode:
        if not root:
            return None
        tree_node = TreeNode(x=root.val)
        if root.children:
            tree_node.left = self.encode(root.children[0])
            other_node = tree_node.left

            for i in range(1, len(root.children)):
                other_node.right = self.encode(root.children[i])
                other_node = other_node.right
        return tree_node

    def decode(self, data: TreeNode) -> Node:
        if not data:
            return None

        node = Node(val=data.val)
        node.children = []
        if data.left is None:
            return node

        other_node = data.left

        while other_node:
            node.children.append(self.decode(other_node))
            other_node = other_node.right
        return node
