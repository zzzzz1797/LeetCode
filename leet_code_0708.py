"""
    给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环非降序的。给定的可以是这个列表中任
意一个顶点的指针，并不一定是这个列表中最小元素的指针。如果有多个满足条件的插入位置，你可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。
如果列表为空（给定的节点是 null），你需要创建一个循环有序列表并返回这个节点。否则，请返回原先给定的节点。

    示例 2：
        输入：head = [], insertVal = 1
        输出：[1]
        解释：列表为空（给定的节点是 null），创建一个循环有序列表并返回这个节点。

    示例 3：
        输入：head = [1], insertVal = 0
        输出：[1,0]

"""


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        return self.answer_1(head, insertVal)

    def answer_1(self, head, insertVal):
        node = Node(val=insertVal)
        if not head:
            node.next = node
            return node

        curr = head.next

        while curr != head:
            if curr.val <= insertVal <= curr.next.val:
                break
            if curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break
                curr = curr.next

        node.next = curr.next
        curr.next = node
        return head
