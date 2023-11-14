"""
    有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，请你按下述规则为栅栏设计涂色方案：
        每个栅栏柱可以用其中 一种 颜色进行上色。
        相邻的栅栏柱 最多连续两个 颜色相同。

    给你两个整数 k 和 n ，返回所有有效的涂色 方案数 。

    示例 1：
        输入：n = 3, k = 2
        输出：6
        解释：所有的可能涂色方案如上图所示。注意，全涂红或者全涂绿的方案属于无效方案，因为相邻的栅栏柱 最多连续两个 颜色相同。

    示例 2：
        输入：n = 1, k = 1
        输出：1

    示例 3：
        输入：n = 7, k = 2
        输出：42

https://leetcode.cn/problems/paint-fence/description
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:
        return self.answer_1(n, k)

    def answer_1(self, n, k):

        memo = {}

        def _dfs(i):
            if i == 1:
                return k
            if i == 2:
                return k * k

            if i in memo:
                return memo[i]

            memo[i] = (k - 1) * (_dfs(i - 1) + _dfs(i - 2))
            return memo[i]

        return _dfs(n)
