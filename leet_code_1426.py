"""
    给你一个整数数组 arr， 对于元素 x ，只有当 x + 1 也在数组 arr 里时，才能记为 1 个数。如果数组 arr 里有重复的数，每个重复的数单独计算。

    示例 1：
        输入：arr = [1,2,3]
        输出：2
        解释：1 和 2 被计算次数因为 2 和 3 在数组 arr 里。

    示例 2：
        输入：arr = [1,1,3,3,5,5,7,7]
        输出：0
        解释：所有的数都不算, 因为数组里没有 2、4、6、8。

    提示：
        1 <= arr.length <= 1000
        0 <= arr[i] <= 1000

"""
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        return self.answer_1(arr)

    def answer_1(self, nums):
        storage = {}

        for num in nums:
            storage[num] = num + 1

        count = 0

        for num in nums:
            if num + 1 in storage:
                count += 1

        return count
