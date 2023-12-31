"""
    给定一个表示任意嵌套三元表达式的字符串 expression ，求值并返回其结果。你可以总是假设给定的表达式是有效的，并且只包含数字，'?'，':'，'T'
和 'F' ，其中 'T' 为真， 'F' 为假。表达式中的所有数字都是 一位 数(即在 [0,9] 范围内)。条件表达式从右到左分组(大多数语言中都是这样)，表达式
的结果总是为数字 'T' 或 'F' 。

    示例 1：
        输入： expression = "T?2:3"
        输出： "2"
        解释： 如果条件为真，结果为 2；否则，结果为 3。

    示例 2：
        输入： expression = "F?1:T?4:5"
        输出： "4"
        解释： 条件表达式自右向左结合。使用括号的话，相当于：
            "(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
            or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"

    示例 3：
        输入： expression = "T?T?F:5:3"
        输出： "F"
        解释： 条件表达式自右向左结合。使用括号的话，相当于：
            "(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
            "(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"
"""


class Solution:
    def parseTernary(self, expression: str) -> str:
        return self.answer_1(expression)

    def answer_1(self, expression):
        stack = []

        index = len(expression) - 1

        stack.append(expression[index])

        while index > 0:
            index -= 1
            if stack[-1] == "?":
                stack.pop()
                flag = expression[index]
                left = stack.pop()
                right = stack.pop()
                if flag == "T":
                    stack.append(left)
                else:
                    stack.append(right)
            else:
                stack.append(expression[index]) if expression[index] != ":" else ...
        return stack[0]
