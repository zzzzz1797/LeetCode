"""
    给你一个的整数数组 nums, 将该数组重新排序后使 nums[0] <= nums[1] >= nums[2] <= nums[3]...
输入数组总是有一个有效的答案。

    示例 1:
        输入：nums = [3,5,2,1,6,4]
        输出：[3,5,1,6,2,4]
        解释：[1,6,2,5,3,4]也是有效的答案

    示例 2:
        输入：nums = [6,6,5,6,3,8]
        输出：[6,6,5,6,3,8]


    提示：
        1 <= nums.length <= 5 * 104
        0 <= nums[i] <= 104
        输入的 nums 保证至少有一个答案。

"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.answer_1(nums)

    def answer_1(self, nums):
        nums.sort()

        for index in range(1, len(nums) - 1, 2):
            tmp_num = nums[index]
            nums[index] = nums[index + 1]
            nums[index + 1] = tmp_num

    def answer_2(self, nums):
        def _swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        for index in range(len(nums) - 1):
            if index % 2 == 0 and nums[index] > nums[index + 1]:
                _swap(index, index + 1)
            if index % 2 == 1 and nums[index] < nums[index + 1]:
                _swap(index, index + 1)
