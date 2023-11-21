"""
    序列化是指将一个数据结构转化为位序列的过程，因此可以将其存储在文件中或内存缓冲区中，以便稍后在相同或不同的计算机环境中恢复结构。设计一个序列
化和反序列化 N 叉树的算法。一个 N 叉树是指每个节点都有不超过 N 个孩子节点的有根树。序列 /反序列化算法的算法实现没有限制。你只需要保证N叉树可以
被序列化为一个字符串并且该字符串可以被反序列化成原树结构即可。

    示例 1:
        输入: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        输出: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

    示例 2:
        输入: root = [1,null,3,2,4,null,5,6]
        输出: [1,null,3,2,4,null,5,6]

    示例 3:
        输入: root = []
        输出: []


    提示：
        树中节点数目的范围是 [0, 104].
        0 <= Node.val <= 104
        N 叉树的高度小于等于 1000
        不要使用类成员 / 全局变量 / 静态变量来存储状态。你的序列化和反序列化算法应是无状态的。
https://leetcode.cn/problems/serialize-and-deserialize-n-ary-tree
"""

from collections import deque


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


class Codec:

    def serialize(self, root: Node) -> str:
        if root == None:
            return "#"
        data = deque([str(root.val), str(len(root.children))])

        for child in root.children:
            data.append(self.serialize(child))
        return "-".join(data)

    def deserialize(self, data: str) -> Node:
        if data == "#":
            return None

        records = deque(data.split("-"))

        return self._dfs(records)

    def _dfs(self, records):
        if not records:
            return None

        val = int(records.popleft())
        children_cnt = records.popleft()

        node = Node(val=val)

        for index in range(children_cnt):
            node.children.append(self._dfs(records))
        return node
