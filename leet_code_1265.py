"""
    给您一个不可变的链表，使用下列接口逆序打印每个节点的值：
        ImmutableListNode: 描述不可变链表的接口，链表的头节点已给出。
    您需要使用以下函数来访问此链表（您 不能 直接访问 ImmutableListNode）：
        ImmutableListNode.printValue()：打印当前节点的值。
        ImmutableListNode.getNext()：返回下一个节点。
    输入只用来内部初始化链表。您不可以通过修改链表解决问题。也就是说，您只能通过上述 API 来操作链表。

    示例 1：
        输入：head = [1,2,3,4]
        输出：[4,3,2,1]

    示例 2：
        输入：head = [0,-4,-1,3,-5]
        输出：[-5,3,-1,-4,0]

    示例 3：
        输入：head = [-2,0,6,4,4,-6]
        输出：[-6,4,4,6,0,-2]

"""


class ImmutableListNode:
    def printValue(self) -> None:  # print the value of this node.
        pass

    def getNext(self) -> 'ImmutableListNode':  # return the next node.
        pass


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
