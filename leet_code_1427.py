"""
    给定一个包含小写英文字母的字符串 s 以及一个矩阵 shift，其中 shift[i] = [direction, amount]：direction 可以为 0 （表示左移）或
1 （表示右移）。amount 表示 s 左右移的位数。左移 1 位表示移除 s 的第一个字符，并将该字符插入到 s 的结尾。类似地，右移 1 位表示移除 s 的最
后一个字符，并将该字符插入到 s 的开头。对这个字符串进行所有操作后，返回最终结果。



    示例 1：
        输入：s = "abc", shift = [[0,1],[1,2]]
        输出："cab"
        解释：
            [0,1] 表示左移 1 位。 "abc" -> "bca"
            [1,2] 表示右移 2 位。 "bca" -> "cab"

    示例 2：
        输入：s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
        输出："efgabcd"
        解释：
        [1,1] 表示右移 1 位。 "abcdefg" -> "gabcdef"
        [1,1] 表示右移 1 位。 "gabcdef" -> "fgabcde"
        [0,2] 表示左移 2 位。 "fgabcde" -> "abcdefg"
        [1,3] 表示右移 3 位。 "abcdefg" -> "efgabcd"

"""
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        return self.answer_1(s, shift)

    def answer_1(self, s, shift):
        def _shift_left(info):
            return info[1:] + info[0]

        def _shift_right(info):
            return info[-1] + info[0: len(info) - 1]

        for direction, amount in shift:
            if direction == 0:
                for i in range(amount):
                    s = _shift_left(s)
            else:
                for i in range(amount):
                    s = _shift_right(s)
        return s

    def anwser_2(self, s, shift):
        steps = 0

        for direction, amount in shift:
            if direction == 0:
                steps += amount
            else:
                steps -= amount

        steps %= len(s)

        if steps == s:
            return s

        return s[steps:] + s[:steps]


if __name__ == '__main__':
    data = Solution().answer_1("abc", [[0, 1], [1, 2]])

    print(data)
