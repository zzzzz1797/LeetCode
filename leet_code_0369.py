"""
    给定一个用链表表示的非负整数， 然后将这个整数 再加上 1 。这些数字的存储是这样的：最高位有效的数字位于链表的首位 head 。

    示例 1:
        输入: head = [1,2,3]
        输出: [1,2,4]

    示例 2:
        输入: head = [0]
        输出: [1]


    提示：
        链表中的节点数在 [1, 100] 的范围内。
        0 <= Node.val <= 9
        由链表表示的数字不包含前导零，除了零本身。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        return self.answer_1(head)

    def answer_1(self, head):
        root = head
        stack = []

        while root:
            stack.append(root)
            root = root.next

        while stack:
            node = stack.pop()
            if node.val == 9:
                node.val = 0
            else:
                node.val += 1
                return head
        return ListNode(1, next=head)

    def answer_2(self, head):
        dummy = ListNode(val=0, next=head)
        most_right = dummy

        while head:
            if head.val != 9:
                most_right = head
            head = head.next

        most_right.val += 1
        most_right = most_right.next

        while most_right:
            most_right.val = 0
            most_right = most_right.next

        return dummy if dummy.val else dummy.next
