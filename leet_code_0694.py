"""
    给定一个非空 01 二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。
    请你计算这个网格中共有多少个形状不同的岛屿。两个岛屿被认为是相同的，当且仅当一个岛屿可以通过平移变换（不可以旋转、翻转）和另一个岛屿重合。


    示例 1：
        输入: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
        输出：1

    示例 2：
        输入: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
        输出: 3
"""
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        return self.answer_1(grid)

    def answer_1(self, grid):
        row_len = len(grid)
        col_len = len(grid[0])

        def _dfs(row, col, origin_row, origin_col, result):
            if row < 0 or col < 0 or row >= row_len or col >= col_len:
                return

            if (row, col) in seen or grid[row][col] == 0:
                return
            result.add((row - origin_row, col - origin_col))

            _dfs(row + 1, col, origin_row, origin_col, result)
            _dfs(row - 1, col, origin_row, origin_col, result)
            _dfs(row, col + 1, origin_row, origin_col, result)
            _dfs(row, col - 1, origin_row, origin_col, result)

        seen = set()
        unique_islands = set()
        for row in range(row_len):
            for col in range(col_len):
                current_island = set()
                row_origin = row
                col_origin = col

                _dfs(row, col, row_origin, col_origin, current_island)

                if current_island:
                    unique_islands.add(frozenset(current_island))

        return len(unique_islands)
