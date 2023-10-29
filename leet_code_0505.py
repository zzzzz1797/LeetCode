"""
    迷宫中有一个球，它有空地 (表示为 0) 和墙 (表示为 1)。球可以向上、向下、向左或向右滚过空地，但直到撞上墙之前它都不会停止滚动。当球停止时，
它才可以选择下一个滚动方向。
    给定 m × n 的迷宫(maze)，球的起始位置 (start = [startrow, startcol]) 和目的地 (destination = [destinationrow, destinationcol])，
返回球在目的地 (destination) 停止的最短距离。如果球不能在目的地 (destination) 停止，返回 -1。
    距离是指球从起始位置 ( 不包括 ) 到终点 ( 包括 ) 所经过的空地数。
    你可以假设迷宫的边界都是墙 ( 见例子 )。



"""
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        return self.answer_1(maze, start, destination)

    def answer_1(self, maze, start, destination):
        row_len, col_len = len(maze), len(maze[0])

        dist = [[float("inf") for _ in range(col_len)] for _ in range(row_len)]
        dist[start[0]][start[1]] = 0

        queue = deque([(start[0], start[1])])

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = r + dr
                nc = c + dc

                step = 1

                while 0 <= nr < row_len and 0 <= nc < col_len and maze[nr][nc] == 0:
                    nr += dr
                    nc += dc
                    step += 1

                nr -= dr
                nc -= dc

                step -= 1

                if dist[r][c] + step < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + step
                    queue.append((nr, nc))

        if dist[destination[0]][destination[1]] == float("inf"):
            return -1
        return dist[destination[0]][destination[1]]
