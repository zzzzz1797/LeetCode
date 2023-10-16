"""
    给你一个大小为 m x n 的图像 picture ，图像由黑白像素组成，'B' 表示黑色像素，'W' 表示白色像素，请你统计并返回图像中 黑色 孤独像素的数量。
黑色孤独像素 的定义为：如果黑色像素 'B' 所在的同一行和同一列不存在其他黑色像素，那么这个黑色像素就是黑色孤独像素。
"""
from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        return self.anwser_1(picture)

    def answer_2_(self, picture):
        result = 0
        row_len, col_len = len(picture), len(picture[0])
        tmp_row, tmp_col = [0 for i in range(row_len)], [0 for i in range(col_len)]

        for row_index in range(row_len):
            for col_index in range(col_len):
                if picture[row_index][col_index] != "B":
                    continue
                tmp_row[row_index] += 1
                tmp_col[col_index] += 1

        for index in range(row_len):
            if tmp_row[index] != 1:
                continue
            for jndex in range(col_len):
                if tmp_col[jndex] != 1:
                    continue
                if picture[index][jndex] != "B":
                    continue
                result += 1
        return result

    def anwser_1(self, picture):
        result = 0

        row_len = len(picture)
        col_len = len(picture[0])

        for row_index in range(row_len):
            for col_index in range(col_len):
                if picture[row_index][col_index] == "B":
                    # 检查行
                    tmp_row = tmp_col = 0
                    for i in range(col_len):
                        if picture[row_index][i] == "B":
                            tmp_row += 1

                    # 检查列
                    for j in range(row_len):
                        if picture[j][col_index] == "B":
                            tmp_col += 1

                    if tmp_col == 1 and tmp_row == 1:
                        result += 1
        return result


if __name__ == '__main__':
    data = Solution().anwser_1([["B", "B", "B"]])
    print(data)
