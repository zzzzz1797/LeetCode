"""
    在某个数组 arr 中，值符合等差数列的数值规律：在 0 <= i < arr.length - 1 的前提下，arr[i+1] - arr[i] 的值都相等。我们会从该数组中删
除一个 既不是第一个 也 不是最后一个的值，得到一个新的数组  arr。
    给你这个缺值的数组 arr，返回 被删除的那个数 。


    示例 1：
        输入：arr = [5,7,11,13]
        输出：9
        解释：原来的数组是 [5,7,9,11,13]。

    示例 2：
        输入：arr = [15,13,12]
        输出：14
        解释：原来的数组是 [15,14,13,12]。
"""
from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return self.answer_1(arr)

    def answer_1(self, arr):
        arr_len = len(arr)

        diff = (arr[-1] - arr[0]) // arr_len

        for index in range(arr_len - 1, 0, -1):
            if arr[index] - arr[index - 1] != diff:
                return arr[index] - diff
        return arr[0]

    def answer_2(self, arr):
        arr_len = len(arr)
        diff = (arr[-1] - arr[0]) // arr_len

        left = 0
        right = arr_len - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] == arr[0] + mid * diff:
                left = mid + 1
            else:
                right = mid

        return arr[0] + diff * left
