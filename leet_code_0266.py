"""
    给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。

    示例 1：
        输入: "code"
        输出: false

    示例 2：
        输入: "aab"
        输出: true

    示例 3：
        输入: "carerac"
        输出: true
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        pass

    def answer_1(self, s):
        storage = {}

        for char in s:
            if char not in storage:
                storage[char] = 1
            else:
                storage[char] += 1

        odd = 0

        for value in list(storage.values()):
            if value % 2 == 1:
                odd += 1
            if odd > 1:
                return False
        return True
