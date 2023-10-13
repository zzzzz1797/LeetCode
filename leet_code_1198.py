"""
    给你一个 m x n 的矩阵 mat，其中每一行的元素均符合 严格递增 。请返回 所有行中的 最小公共元素 。如果矩阵中没有这样的公共元素，就请返回-1。

    示例 1：
        输入：mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
        输出：5

    示例 2:
        输入：mat = [[1,2,3],[2,3,4],[2,3,5]]
        输出： 2

    提示：
        m == mat.length
        n == mat[i].length
        1 <= m, n <= 500
        1 <= mat[i][j] <= 104
        mat[i] 已按严格递增顺序排列。
"""
from collections import defaultdict
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        return self.answer_1(mat)

    def answer_1(self, mat):
        storage = defaultdict(int)

        min_value, max_value = float("inf"), float("-inf")
        row_len, col_len = len(mat), len(mat[0])

        for row_index in range(row_len):
            for col_index in range(col_len):
                value = mat[row_index][col_index]
                storage[value] += 1
                min_value = min(min_value, value)
                max_value = max(max_value, value)

        for index in range(min_value, max_value + 1):
            if storage[index] == row_len:
                return index
        return -1


if __name__ == '__main__':
    print(Solution().answer_1([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]))
