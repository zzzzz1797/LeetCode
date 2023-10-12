"""
    给定字符串 s 和 t ，判断 s 是否为 t 的子序列。字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新
字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

    进阶：
        如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？


    示例 1：
        输入：s = "abc", t = "ahbgdc"
        输出：true

    示例 2：
        输入：s = "axc", t = "ahbgdc"
        输出：false

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return self.answer_1(s, t)

    def answer_1(self, s, t):
        s_len, t_len = len(s), len(t)

        s_index = t_index = 0

        while s_index < s_len and t_index < t_len:

            if s[s_index] == t[t_index]:
                s_index += 1

            t_index += 1
        return s_index == s_len

    def answer_2(self, s, t):
        pass
