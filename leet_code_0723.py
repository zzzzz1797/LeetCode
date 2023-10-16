"""
    这个问题是实现一个简单的消除算法。给定一个 m x n 的二维整数数组 board 代表糖果所在的方格，不同的正整数 board[i][j] 代表不同种类的糖果，如果 board[i][j] == 0 代表 (i, j)
这个位置是空的。
    给定的方格是玩家移动后的游戏状态，现在需要你根据以下规则粉碎糖果，使得整个方格处于稳定状态并最终输出：
        如果有三个及以上水平或者垂直相连的同种糖果，同一时间将它们粉碎，即将这些位置变成空的。
        在同时粉碎掉这些糖果之后，如果有一个空的位置上方还有糖果，那么上方的糖果就会下落直到碰到下方的糖果或者底部，这些糖果都是同时下落，
    也不会有新的糖果从顶部出现并落下来。
    通过前两步的操作，可能又会出现可以粉碎的糖果，请继续重复前面的操作。当不存在可以粉碎的糖果，也就是状态稳定之后，请输出最终的状态。你需要模
拟上述规则并使整个方格达到稳定状态，并输出。
"""
from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        return self.answer_1(board)

    def answer_1(self, board):
        row_len = len(board)
        col_len = len(board[0])

        to_do = False

        # 标记
        for row_index in range(row_len):
            for col_index in range(col_len - 2):
                current_num = abs(board[row_index][col_index])
                second_num = abs(board[row_index][col_index + 1])
                third_num = abs(board[row_index][col_index + 2])

                if not (current_num == second_num == third_num and current_num != 0):
                    continue

                to_do = True

                board[row_index][col_index] = -current_num
                board[row_index][col_index + 1] = -current_num
                board[row_index][col_index + 2] = -current_num

        for row_index in range(row_len - 2):
            for col_index in range(col_len):
                current_num = abs(board[row_index][col_index])
                second_num = abs(board[row_index + 1][col_index])
                third_num = abs(board[row_index + 2][col_index])

                if not (current_num == second_num == third_num and current_num != 0):
                    continue

                to_do = True

                board[row_index][col_index] = -current_num
                board[row_index + 1][col_index] = -current_num
                board[row_index + 2][col_index] = -current_num

        # 清除
        for col_index in range(col_len):
            tmp_row_index = row_len - 1
            for row_index in range(row_len - 1, -1, -1):
                if board[row_index][col_index] > 0:
                    board[tmp_row_index][col_index] = board[row_index][col_index]
                    tmp_row_index -= 1

            for row_index in range(tmp_row_index , -1, -1):
                board[row_index][col_index] = 0
        return self.answer_1(board) if to_do else board
