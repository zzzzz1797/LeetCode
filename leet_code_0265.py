"""
    假如有一排房子共有n幢，每个房子可以被粉刷成k种颜色中的一种。房子粉刷成不同颜色的花费成本也是不同的。你需要粉刷所有的房子并且使其相邻的两个
房子颜色不能相同。
    每个房子粉刷成不同颜色的花费以一个 n x k 的矩阵表示。
    例如，costs[0][0] 表示第 0 幢房子粉刷成 0 号颜色的成本；costs[1][2] 表示第 1 幢房子粉刷成 2 号颜色的成本，以此类推。返回粉刷完所有房
子的最低成本 。


    示例 1：
        输入: costs = [[1,5,3],[2,9,4]]
        输出: 5
        解释:
            将房子 0 刷成 0 号颜色，房子 1 刷成 2 号颜色。花费: 1 + 4 = 5;
            或者将 房子 0 刷成 2 号颜色，房子 1 刷成 0 号颜色。花费: 3 + 2 = 5.

    示例 2:
        输入: costs = [[1,3],[2,4]]
        输出: 5

https://leetcode.cn/problems/paint-house-ii/description
"""
from functools import lru_cache
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        return self.answer_1(costs)

    def answer_1(self, costs):
        n = len(costs)
        if n == 0:
            return 0

        k = len(costs[0])

        @lru_cache(maxsize=None)
        def _memo_resolve(house_index, color):
            if house_index == n - 1:
                return color[house_index][color]

            tmp_cost = float("inf")

            for next_color in range(k):
                if next_color == color:
                    continue

                tmp_cost = min(tmp_cost, _memo_resolve(house_index + 1, next_color))
            return costs[house_index][color] + tmp_cost

        cost = float("inf")

        for index in range(k):
            cost = min(cost, _memo_resolve(0, index))
        return cost

    def answer_2(self, costs):
        n = len(costs)
        if n == 0:
            return 0

        k = len(costs[0])

        for index in range(1, n):
            for color in range(k):
                best = float('inf')
                for other_color in range(k):
                    if other_color == color:
                        continue
                    best = min(best, costs[index - 1][other_color])
                costs[index][color] += best

        return min(costs[-1])
