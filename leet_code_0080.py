"""

    给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。不要使用额外的数组空
间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

    示例 1：
        输入：nums = [1,1,1,2,2,3]
        输出：5, nums = [1,1,2,2,3]
        解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。

    示例 2：
        输入：nums = [0,0,1,1,1,1,2,3,3]
        输出：7, nums = [0,0,1,1,2,3,3]
        解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。

https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii
"""
import collections
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.answer_1(nums)

    def answer_1(self, nums):
        mapper = collections.defaultdict(int)
        times = 2

        move_index = 0
        for index, row in enumerate(nums):
            mapper[row] += 1

            if mapper[row] <= times:
                nums[move_index] = row
                move_index += 1

        return move_index

    def answer_2(self, nums):

        last_num = nums[0]
        last_num_times = 1

        move_index = 1
        index = 1

        times = 2
        length = len(nums)

        while index < length:
            num = nums[index]

            if num == last_num:
                last_num_times += 1
            else:
                last_num_times = 1
                last_num = num

            if last_num_times <= times:
                nums[move_index] = nums[index]
                move_index += 1

            index += 1

        return move_index
