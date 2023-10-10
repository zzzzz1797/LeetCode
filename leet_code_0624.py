"""
    给定 m 个数组，每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和
b 之间的距离定义为它们差的绝对值 |a-b| 。你的任务就是去找到最大距离。

    示例 1：
        输入：
            [
                [1,2,3],
                [4,5],
                [1,2,3]
            ]
        输出： 4
        解释： 一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。


    注意：
        每个给定数组至少会有 1 个数字。列表中至少有两个非空数组。
        所有 m 个数组中的数字总数目在范围 [2, 10000] 内。
        m 个数组中所有整数的范围在 [-10000, 10000] 内。
"""
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        return self.answer_1(arrays)

    def answer_1(self, arrays):
        max_val, min_val = arrays[0][-1], arrays[0][0]

        result = float("-inf")

        for array in arrays[1:]:
            result = max(array[-1] - min_val, result)
            result = max(max_val - array[0], result)

            max_val = max(array[-1], max_val)
            min_val = min(array[0], min_val)

        return result
