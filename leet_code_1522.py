"""
    给定一棵 N 叉树的根节点root，计算这棵树的直径长度。N 叉树的直径指的是树中任意两个节点间路径中最长路径的长度。这条路径可能经过根节点，也可
能不经过根节点。（N 叉树的输入序列以层序遍历的形式给出，每组子节点用 null 分隔）


    示例 1：
        输入：root = [1,null,3,2,4,null,5,6]
        输出：3

    示例 2：
        输入：root = [1,null,2,null,3,4,null,5,null,6]
        输出：4

"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: Node) -> int:
        return self.answer_1(root)

    def answer_1(self, root):
        result = 0

        def _dfs(node):
            if not node:
                return 0
            if not node.children:
                return 1

            child_count = len(node.children)

            max1 = max2 = 0
            memo = [0] * child_count

            for index in range(child_count):
                val = _dfs(node.children[index])

                memo[index] = val

                if val > max1:
                    max1, max2 = val, max1
                elif val > max2:
                    max2 = val
            nonlocal result
            result = max(result, max1 + max2)
            return max1 + 1

        _dfs(root)

        return result
