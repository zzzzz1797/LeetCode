"""
   给你一个字符数组 s ，反转其中 单词 的顺序。单词 的定义为：单词是一个由非空格字符组成的序列。s 中的单词将会由单个空格分隔。必须设计并实现 原地
解法来解决此问题，即不分配额外的空间。


    示例 1：
        输入：s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
        输出：["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

    示例 2：
        输入：s = ["a"]
        输出：["a"]


    提示：
        1 <= s.length <= 105
        s[i] 可以是一个英文字母（大写或小写）、数字、或是空格 ' ' 。
        s 中至少存在一个单词
        s 不含前导或尾随空格
        题目数据保证：s 中的每个单词都由单个空格分隔
"""
from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.answer_1(s)

    def answer_1(self, s):
        """
        先对每一个单词实现翻转，再对整个数组实现翻转。
        这样单词实现了两次翻转，所以单词个体的顺序仍不变，但单词间的顺序发生了变化。
        """
        i = 0
        s_len = len(s)
        for index in range(s_len):
            if s[index] != " ":
                continue
            self._reverse(s, i, index)
            i = index + 1
        self._reverse(s, i, s_len)
        self._reverse(s, 0, s_len)

    @classmethod
    def _reverse(cls, s, i, j):
        l, r = i, j - 1
        while l < r:
            s[l], s[r] = s[r], s[l]

            l += 1
            r -= 1


if __name__ == '__main__':
    gs = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    Solution().answer_1(gs)
    print(gs)
