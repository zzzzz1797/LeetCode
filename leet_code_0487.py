"""
    给定一个二进制数组 nums ，如果最多可以翻转一个 0 ，则返回数组中连续 1 的最大个数。

    示例 1：
        输入：nums = [1,0,1,1,0]
        输出：4
        解释：翻转第一个 0 可以得到最长的连续 1。
             当翻转以后，最大连续 1 的个数为 4。

    示例 2:
        输入：nums = [1,0,1,1,0,1]
        输出：4


    提示:
        1 <= nums.length <= 105
        nums[i] 不是 0 就是 1.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return self.answer_1(nums)

    def answer_1(self, nums):
        left = current_zero_num = result = 0

        for index, num in enumerate(nums):
            if num == 0:
                current_zero_num += 1
            while current_zero_num > 1:
                if num[left] == 0:
                    current_zero_num -= 1
                left += 1
            result = max(result, index - left + 1)
        return result
