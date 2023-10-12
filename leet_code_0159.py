"""
给你一个字符串 s ，请你找出 至多 包含 两个不同字符 的最长子串，并返回该子串的长度。

    示例 1：
        输入：s = "eceba"
        输出：3
        解释：满足题目要求的子串是 "ece" ，长度为 3 。

    示例 2：
        输入：s = "ccaabbb"
        输出：5
        解释：满足题目要求的子串是 "aabbb" ，长度为 5 。

    提示：
        1 <= s.length <= 105
        s 由英文字母组成
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        return self.answer_1(s)

    def answer_1(self, s):
        s_len = len(s)

        if s_len < 3:
            return s_len

        left = right = 0

        storage = {}

        max_len = 2

        while right < s_len:
            storage[s[right]] = right
            right += 1

            if len(storage) == 3:
                del_index = min(storage.values())
                del storage[s[del_index]]
                left = del_index + 1

            max_len = max(max_len, right - left)
        return max_len
