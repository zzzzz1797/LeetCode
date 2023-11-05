"""
    给定一个 n 个元素有序的（升序）整型数组nums和一个目标值 target，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

    示例 1:
        输入: nums = [-1,0,3,5,9,12], target = 9
        输出: 4
        解释: 9 出现在 nums 中并且下标为 4

    示例 2:
        输入: nums = [-1,0,3,5,9,12], target = 2
        输出: -1
        解释: 2 不存在 nums 中因此返回 -1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.answer_1(nums, target)

    def answer_1(self, nums, target):

        for index, num in enumerate(nums):
            if num == target:
                return index
        return -1

    def answer_2(self, nums, target):
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2

            tmp_target = nums[mid]

            if tmp_target == target:
                start = mid
            elif tmp_target > target:
                end = mid - 1
            elif tmp_target < target:
                start = mid
        if len(nums) == end or nums[end] != target:
            return -1
        return end

    def answer_3(self, nums, target):
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2

            tmp_target = nums[mid]

            if tmp_target == target:
                end = mid
            elif tmp_target > target:
                end = mid
            elif tmp_target < target:
                start = mid + 1

        if len(nums) == start or nums[start] != target:
            return -1
        return end
