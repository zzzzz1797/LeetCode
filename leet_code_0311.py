"""
    给定两个 稀疏矩阵 ：大小为 m x k 的稀疏矩阵 mat1 和大小为 k x n 的稀疏矩阵 mat2 ，返回 mat1 x mat2 的结果。你可以假设乘法总是可能的。

    示例 1：
        输入：mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
        输出：[[7,0,0],[-7,0,3]]

    示例 2:
        输入：mat1 = [[0]], mat2 = [[0]]
        输出：[[0]]


    矩阵乘法是一种二元运算，当两个矩阵相乘时，其输出是另一个矩阵。要乘以两个矩阵，两个矩阵必须兼容，这里的兼容性意味着，如果我们有两个矩阵 AAA
和 BBB，那么要计算 A⋅BA \cdot BA⋅B， A的列数应等于B的行数。并且，结果矩阵将具有等于 A 的行数乘以 B 的列数的大小。

"""
from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        return self.answer_1(mat1, mat2)

    def answer_1(self, mat1, mat2):
        mat1_row = len(mat1)
        mat2_col = len(mat2[0])

        result = [[0 for i in range(mat2_col)] for i in range(mat1_row)]

        for row_index, row_element in enumerate(mat1):
            for col_index, col_element in enumerate(row_element):
                if not col_element:
                    continue
                for mat2_index, mat2_element in enumerate(mat2[col_index]):
                    result[row_index][mat2_index] += col_element * mat2_element
        return result
