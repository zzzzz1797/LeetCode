"""
    给定两个列表 A and B，并且 B 是 A 的变位（即 B 是由 A 中的元素随机排列后组成的新列表）。我们希望找出一个从 A 到 B 的索引映射 P 。一个
映射 P[i] = j 指的是列表 A 中的第 i 个元素出现于列表 B 中的第 j 个元素上。列表 A 和 B 可能出现重复元素。如果有多于一种答案，输出任意一种。
例如，给定
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
需要返回 [1, 4, 3, 2, 0]，P[0] = 1 ，因为 A 中的第 0 个元素出现于 B[1]，而且 P[1] = 4 因为 A 中第 1 个元素出现于 B[4]，以此类推。

注：
    A, B 有相同的长度，范围为 [1, 100]。
    A[i], B[i] 都是范围在 [0, 10^5] 的整数。

"""
from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.anwser(nums1, nums2)

    def anwser(self, nums1, nums2):
        mapper = {num: index for index, num in enumerate(nums2)}
        return [mapper[num] for num in nums1]
