"""
    给定一个整数n，返回所有长度为 n 的 中心对称数 。你可以以任何顺序返回答案。中心对称数 是一个数字在旋转了 180 度之后看起来依旧相同的数字（
或者上下颠倒地看）。

    示例 1:
        输入：n = 2
        输出：["11","69","88","96"]

    示例 2:
        输入：n = 1
        输出：["0","1","8"]


    提示：
        1 <= n <= 14

https://leetcode.cn/problems/strobogrammatic-number-ii
"""
from typing import List


class Solution:
    _PAIRS = [("1", "1"), ("8", "8"), ("9", "6"), ("6", "9")]

    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.answer_1(n)

    def answer_1(self, n):
        def _dfs(cur_len):
            if cur_len == 0:
                return [""]

            if cur_len == 1:
                return ["0", "1", "8"]

            result = []

            for num in _dfs(cur_len - 2):
                for l, r in self._PAIRS:
                    result.append(l + num + r)

                if cur_len != n:
                    result.append("0" + num + "0")
            return result

        return _dfs(n)
