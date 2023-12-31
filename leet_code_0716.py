"""
    设计一个最大栈数据结构，既支持栈操作，又支持查找栈中最大元素。
    实现 MaxStack 类：
        MaxStack() 初始化栈对象
        void push(int x) 将元素 x 压入栈中。
        int pop() 移除栈顶元素并返回这个元素。
        int top() 返回栈顶元素，无需移除。
        int peekMax() 检索并返回栈中最大元素，无需移除。
        int popMax() 检索并返回栈中最大元素，并将其移除。如果有多个最大元素，只要移除 最靠近栈顶 的那个。

    示例：
        输入
            ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
            [[], [5], [1], [5], [], [], [], [], [], []]
        输出
            [null, null, null, null, 5, 5, 1, 5, 1, 5]

        解释
            MaxStack stk = new MaxStack();
            stk.push(5);   // [5] - 5 既是栈顶元素，也是最大元素
            stk.push(1);   // [5, 1] - 栈顶元素是 1，最大元素是 5
            stk.push(5);   // [5, 1, 5] - 5 既是栈顶元素，也是最大元素
            stk.top();     // 返回 5，[5, 1, 5] - 栈没有改变
            stk.popMax();  // 返回 5，[5, 1] - 栈发生改变，栈顶元素不再是最大元素
            stk.top();     // 返回 1，[5, 1] - 栈没有改变
            stk.peekMax(); // 返回 5，[5, 1] - 栈没有改变
            stk.pop();     // 返回 1，[5] - 此操作后，5 既是栈顶元素，也是最大元素
            stk.top();     // 返回 5，[5] - 栈没有改变
"""

from sortedcontainers import SortedList


class MaxStackV1:

    def __init__(self):
        self._index = 0
        self._storage = {}
        self._sort_list = SortedList()

    def push(self, x: int) -> None:
        self._storage[self._index] = x
        self._sort_list.add((x, self._index))
        self._index += 1

    def pop(self) -> int:
        index, x = self._storage.popitem()
        self._sort_list.remove((x, index))
        return x

    def top(self) -> int:
        return next(reversed(self._storage.values()))

    def peekMax(self) -> int:
        return self._sort_list[-1][0]

    def popMax(self) -> int:
        x, index = self._sort_list.pop()
        self._storage.pop(index)
        return x


class MaxStack:

    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        self._stack.append((x, max(self._stack[-1][1], x) if self._stack else x))

    def pop(self) -> int:
        return self._stack.pop()[0]

    def top(self) -> int:
        return self._stack[-1][0]

    def peekMax(self) -> int:
        return self._stack[-1][1]

    def popMax(self) -> int:
        tmp = []

        max_num = self.peekMax()

        while self.top() != max_num:
            tmp.append(self._stack.pop())

        self._stack.pop()

        while tmp:
            self.push(tmp.pop()[0])
        return max_num


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
