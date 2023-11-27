"""
    给你一个 非严格递增排列的数组nums，请你原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。元素的相对顺序应该保持一致。然
后返回 nums 中唯一元素的个数。

    示例 1：
        输入：nums = [1,1,2]
        输出：2, nums = [1,2,_]
        解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

    示例 2：
        输入：nums = [0,0,1,1,1,2,2,3,3,4]
        输出：5, nums = [0,1,2,3,4]
        解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        move_index = 0

        for index, row in range(len(nums)):
            if move_index == 0 or nums[index] != nums[index - 1]:
                nums[move_index] = nums[index]
                move_index += 1
        return move_index
