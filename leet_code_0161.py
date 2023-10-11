"""
    给定两个字符串 s 和 t ，如果它们的编辑距离为 1 ，则返回 true ，否则返回 false 。字符串 s 和字符串 t 之间满足编辑距离等于 1 有三种可能
的情形：
    往 s 中插入 恰好一个 字符得到 t
    从 s 中删除 恰好一个 字符得到 t
    在 s 中用 一个不同的字符 替换 恰好一个 字符得到 t


    示例 1：
        输入: s = "ab", t = "acb"
        输出: true
        解释: 可以将 'c' 插入字符串 s 来得到 t。

    示例 2:
        输入: s = "cab", t = "ad"
        输出: false
        解释: 无法通过 1 步操作使 s 变为 t。
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        return self.answer_1(s, t)

    def answer_1(self, s, t):
        s_len, t_len = len(s), len(t)

        if s_len < t_len:
            return self.answer_1(t, s)

        if s_len - t_len > 1:
            return False

        for index in range(t_len):
            if s[index] != t[index]:
                if s_len == t_len:
                    return s[index + 1:] == t[index + 1:]
                else:
                    return s[index + 1:] == t[index:]
        return t_len + 1 == s_len


if __name__ == '__main__':
    print(Solution().answer_1("cab", "ad"))