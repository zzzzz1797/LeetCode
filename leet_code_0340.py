"""
    给你一个字符串 s 和一个整数 k ，请你找出 至多 包含 k 个 不同 字符的最长子串，并返回该子串的长度。


    示例 1：
        输入：s = "eceba", k = 2
        输出：3
        解释：满足题目要求的子串是 "ece" ，长度为 3 。

    示例 2：
        输入：s = "aa", k = 1
        输出：2
        解释：满足题目要求的子串是 "aa" ，长度为 2 。


    提示：
        1 <= s.length <= 5 * 104
        0 <= k <= 50
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        return self.answer_1(s, k)

    def answer_1(self, s, k):
        s_len = len(s)

        if s_len < k:
            return s_len

        left = right = 0

        result = float("-inf")
        storage = {}

        while right < s_len:
            storage[s[right]] = right

            right += 1

            if len(storage) > k:
                del_index = min(storage.values())
                del storage[s[del_index]]
                left = del_index + 1
            result = max(result, right - left)
        return result

        return result
