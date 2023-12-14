"""
    峰值元素是指其值严格大于左右相邻值的元素。给你一个整数数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个
峰值所在位置即可。
    你可以假设 nums[-1] = nums[n] = -∞ 。
    你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

    示例 1：
        输入：nums = [1,2,3,1]
        输出：2
        解释：3 是峰值元素，你的函数应该返回其索引 2。

    示例 2：
        输入：nums = [1,2,1,3,5,6,4]
        输出：1 或 5
        解释：你的函数可以返回索引 1，其峰值元素为 2；或者返回索引 5， 其峰值元素为 6。

https://leetcode.cn/problems/find-peak-element/
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.answer_1(nums)

    def answer_1(self, nums):
        length = len(nums)

        left = 0
        right = length - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
