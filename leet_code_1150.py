"""
    给出一个按非递减顺序排列的数组nums，和一个目标数值target。假如数组nums中绝大多数元素的数值都等于target，则返回True，否则请返回False。
所谓占绝大多数，是指在长度为 N 的数组中出现必须 超过 N/2 次。

    示例 1：
        输入：nums = [2,4,5,5,5,5,5,6,6], target = 5
        输出：true
        解释：
        数字 5 出现了 5 次，而数组的长度为 9。
        所以，5 在数组中占绝大多数，因为 5 次 > 9/2。

    示例 2：
        输入：nums = [10,100,101,101], target = 101
        输出：false
        解释：
        数字 101 出现了 2 次，而数组的长度是 4。
        所以，101 不是 数组占绝大多数的元素，因为 2 次 = 4/2。
"""
from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return self.answer_1(nums, target)

    def answer_1(self, nums, target):
        cnt = 0

        for num in nums:
            if num == target:
                cnt += 1

        return cnt > len(nums) // 2

    def answer_2(self, nums, target):

        def _search_left():
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2
                cmp_target = nums[mid]
                if cmp_target == target:
                    end = mid - 1
                elif cmp_target < target:
                    start = mid + 1
                elif cmp_target > target:
                    end = mid - 1
            return start

        def _search_right():
            start = 0
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2
                cmp_target = nums[mid]
                if cmp_target == target:
                    start = mid + 1
                elif cmp_target < target:
                    start = mid + 1
                elif cmp_target > target:
                    end = mid - 1
            return end

        left = _search_left()
        right = _search_right()

        return (right - left + 2) > len(nums) // 2


if __name__ == '__main__':
    data = Solution().answer_2([10, 100, 101, 101], 2)
    print(data)
