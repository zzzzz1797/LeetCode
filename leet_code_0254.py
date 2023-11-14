"""
    整数可以被看作是其因子的乘积。

    例如：

        8 = 2 x 2 x 2;
          = 2 x 4.
    请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。

    注意：
        你可以假定 n 为永远为正数。
        因子必须大于 1 并且小于 n。

    示例 1：
        输入: 1
        输出: []

    示例 2：
        输入: 37
        输出: []

    示例 3：
        输入: 12
        输出:
            [
                [2, 6],
                [2, 2, 3],
                [3, 4]
            ]
    示例 4:
        输入: 32
        输出:
            [
                [2, 16],
                [2, 2, 8],
                [2, 2, 2, 4],
                [2, 2, 2, 2, 2],
                [2, 4, 4],
                [4, 8]
            ]
https://leetcode.cn/problems/factor-combinations/description
"""
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        return self.answer_1(n)

    def answer_1(self, n):
        def _dfs(cur_n, l):
            result = []
            i = l

            while i * i <= cur_n:
                if cur_n % i == 0:
                    result.append([i, n // i])
                    for sub_list in _dfs(cur_n // i, i):
                        sub_list.append(i)
                        result.append(sub_list[:])
                i += 1
            return result

        return _dfs(n, 2)


if __name__ == '__main__':
    print(Solution().getFactors(8))
