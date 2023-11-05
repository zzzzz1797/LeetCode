"""
    给你一个整数 n ，让你来判定他是否是 阿姆斯特朗数，是则返回 true，不是则返回 false。假设存在一个k位数 n ，其每一位上的数字的k次幂的总和
也是n，那么这个数是阿姆斯特朗数 。

    示例 1：
        输入：n = 153
        输出：true
        示例：
            153 是一个 3 位数，且 153 = 13 + 53 + 33。

    示例 2：
        输入：n = 123
        输出：false
        解释：123 是一个 3 位数，且 123 != 13 + 23 + 33 = 36。


    提示：
        1 <= n <= 108
"""


class Solution:
    def isArmstrong(self, n: int) -> bool:
        return self.answer_1(n)

    def answer_1(self, n):
        result = 0
        times = 0

        original_n = compute_times_n = compute_result_n = n

        while compute_times_n:
            times += 1
            compute_times_n = compute_times_n // 10

        while compute_result_n:
            result += (compute_result_n % 10) ** times

            compute_result_n = compute_result_n // 10
        return result == original_n
