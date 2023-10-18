"""
    实现一个基本的计算器来计算简单的表达式字符串。表达式字符串只包含非负整数，算符 +、-、*、/ ，左括号 ( 和右括号 ) 。整数除法需要 向下截断 。
你可以假定给定的表达式总是有效的。所有的中间结果的范围均满足 [-231, 231 - 1] 。
    注意：你不能使用任何将字符串作为表达式求值的内置函数，比如 eval() 。

    示例 1：
        输入：s = "1+1"
        输出：2

    示例 2：
        输入：s = "6-4/2"
        输出：4

    示例 3：
        输入：s = "2*(5+5*2)/3+(6/2+8)"
        输出：21
"""


class Solution:
    def calculate(self, s: str) -> int:
        return self.answer_1(s)

    def answer_1(self, s):
        num_stack, opt_stack = [], []

        index, s_len = 0, len(s)

        priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}

        while index < s_len:
            if s[index] == " ":
                index += 1
                continue

            if "0" <= s[index] <= "9":
                start = index

                while index + 1 < s_len and "0" <= s[index + 1] <= "9":
                    index += 1

                num_stack.append(s[start:index + 1])
            elif s[index] == "(":
                opt_stack.append(s[index])
            elif s[index] == ")":
                while opt_stack[-1] != "(":
                    self._execute(opt_stack, num_stack)
                opt_stack.pop()
            else:
                while opt_stack and priority[opt_stack[-1]] >= priority[s[index]]:
                    self._execute(opt_stack, num_stack)
                opt_stack.append(s[index])
            index += 1

        while opt_stack:
            self._execute(opt_stack, num_stack)

        return int(num_stack[-1])

    @classmethod
    def _execute(cls, opt_stack, num_stack):
        opt = opt_stack.pop()
        num1 = num_stack.pop()
        num2 = num_stack.pop()
        result = cls._calc(num1, num2, opt)
        num_stack.append(result)

    @classmethod
    def _calc(cls, num1, num2, opt):
        num1 = int(num1)
        num2 = int(num2)

        if opt == "+":
            return num1 + num2
        elif opt == "-":
            return num2 - num1
        elif opt == "*":
            return num2 * num1
        elif opt == "/":
            return int(num2 / num1)


if __name__ == '__main__':
    data = Solution().calculate("1*2-3/4+5*6-7*8+9/10")
    # 2-0  + 20 - 56 + 0
    # 2 + 20 - 56
    print(data)
