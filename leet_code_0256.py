"""
    假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个nx3的正整数矩阵costs来
表示的。
    例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。
    请计算出粉刷完所有房子最少的花费成本。

    示例 1：
        输入: costs = [[17,2,17],[16,16,5],[14,3,19]]
        输出: 10
        解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。最少花费: 2 + 5 + 3 = 10。

    示例 2：
        输入: costs = [[7,6,2]]
        输出: 2

https://leetcode.cn/problems/paint-house/description
"""
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        return self.answer_1(costs)

    def answer_1(self, costs):
        length = len(costs)

        dp = []
        for i in range(length):
            dp.append([0 for i in range(3)])

        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for index in range(1, length):
            dp[index][0] = min(dp[index - 1][1], dp[index - 1][2]) + costs[index][0]
            dp[index][1] = min(dp[index - 1][0], dp[index - 1][2]) + costs[index][1]
            dp[index][2] = min(dp[index - 1][0], dp[index - 1][1]) + costs[index][2]
        return min(dp[length - 1][0], dp[length - 1][1], dp[length - 1][2])
