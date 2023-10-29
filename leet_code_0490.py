"""
    由空地（用 0 表示）和墙（用 1 表示）组成的迷宫 maze 中有一个球。球可以途经空地向 上、下、左、右 四个方向滚动，且在遇到墙壁前不会停止滚动。
当球停下时，可以选择向下一个方向滚动。给你一个大小为mxn的迷宫maze，以及球的初始位置start 和目的地destination，其中 start = [startrow,
startcol] 且 destination = [destinationrow, destinationcol] 。请你判断球能否在目的地停下：如果可以，返回 true ；否则，返回 false 。

    示例 1：
        输入：maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
        输出：true
        解释：一种可能的路径是 : 左 -> 下 -> 左 -> 下 -> 右 -> 下 -> 右。

    示例 2：
        输入：maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
        输出：false
        解释：不存在能够使球停在目的地的路径。注意，球可以经过目的地，但无法在那里停驻。
"""
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        return self.answer_1(maze, start, destination)

    def answer_1(self, maze, start, destination):
        row_len = len(maze)
        col_len = len(maze[0])

        def dfs(x, y):
            maze[x][y] = -1

            if x == destination[0] and y == destination[1]:
                return True

            res = False
            original_x, original_y = x, y
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = original_x, original_y
                while 0 <= x + dx < row_len and 0 <= y + dy < col_len and (
                    maze[dx + x][dy + y] == 0 or maze[dx + x][dy + y] == -1):
                    x = dx + x
                    y = dy + y

                if maze[x][y] != -1:
                    res = res or dfs(x, y)
            return res

        return dfs(start[0], start[1])
