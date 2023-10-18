"""
给定链表 head 和两个整数 m 和 n. 遍历该链表并按照如下方式删除节点:
    开始时以头节点作为当前节点.
    保留以当前节点开始的前 m 个节点.
    删除接下来的 n 个节点.
    重复步骤 2 和 3, 直到到达链表结尾.
在删除了指定结点之后, 返回修改过后的链表的头节点.


    示例 1:
        输入: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
        输出: [1,2,6,7,11,12]
        解析: 保留前(m = 2)个结点,  也就是以黑色节点表示的从链表头结点开始的结点(1 ->2).
            删除接下来的(n = 3)个结点(3 -> 4 -> 5), 在图中以红色结点表示.
            继续相同的操作, 直到链表的末尾.
            返回删除结点之后的链表的头结点.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, val):
        new_node = self.__class__(val)
        self.next = new_node
        return new_node

    def __str__(self):
        output = []
        root = self
        while root:
            output.append(root.val)
            root = root.next
        return "->".join(map(str, output))


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        return self.answer_1(head, m, n)

    def answer_1(self, head, m, n):
        curr = head
        last = head

        while curr:
            p, q = m, n
            while p and curr:
                last = curr
                curr = curr.next
                p -= 1

            while q and curr:
                curr = curr.next
                q -= 1
            last.next = curr
        return head
