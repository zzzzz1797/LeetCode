"""
    现有一个按升序排列的整数数组nums，其中每个数字都 互不相同 。给你一个整数k，请你找出并返回从数组最左边开始的第 k 个缺失数字。

    示例 1：
        输入：nums = [4,7,9,10], k = 1
        输出：5
        解释：第一个缺失数字为 5 。

    示例 2：
        输入：nums = [4,7,9,10], k = 3
        输出：8
        解释：缺失数字有 [5,6,8,...]，因此第三个缺失数字为 8 。

    示例 3：
        输入：nums = [1,2,4], k = 3
        输出：6
        解释：缺失数字有 [3,5,6,7,...]，因此第三个缺失数字为 6 。

https://leetcode.cn/problems/missing-element-in-sorted-array/description
"""
from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        return self.answer_1(nums, k)

    def answer_1(self, nums, k):
        length = len(nums)

        for index in range(1, length):
            loss = nums[index] - nums[index - 1] - 1

            if loss >= k:
                return nums[index - 1] + k
            else:
                k -= loss
        return nums[length - 1] + k
