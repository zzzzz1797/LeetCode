"""
    给你一个不同学生的分数列表 items，其中 items[i] = [IDi, scorei] 表示IDi的学生的一科分数，你需要计算每个学生 最高的五科成绩的平均分。
返回答案 result 以数对数组形式给出，其中 result[j] = [IDj, topFiveAveragej] 表示IDj的学生和他 最高的五科成绩的平均分。result需要按IDj
递增的 顺序排列 。
    学生 最高的五科 成绩的 平均分 的计算方法是将最高的五科分数相加，然后用 整数除法 除以 5 。


    示例 1：
        输入：items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
        输出：[[1,87],[2,88]]
        解释：
            ID = 1 的学生分数为 91、92、60、65、87 和 100 。前五科的平均分 (100 + 92 + 91 + 87 + 65) / 5 = 87
            ID = 2 的学生分数为 93、97、77、100 和 76 。前五科的平均分 (100 + 97 + 93 + 77 + 76) / 5 = 88.6，但是由于使用整数除法，
            结果转换为 88

    示例 2：
        输入：items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
        输出：[[1,100],[7,100]]

"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        return self.answer_1(items)

    def answer_1(self, items):
        storage = defaultdict(list)

        for idx, score in items:
            q = storage[idx]
            if len(q) > 5:
                heapq.heappop(q)
            heapq.heappush(q, score)

        keys = sorted(storage.keys())

        result = []
        for key in keys:
            q = storage[key]
            if len(q) > 5:
                heapq.heappop(q)
            result.append([key, sum(storage[key]) // len(storage[key])])

        return result


if __name__ == '__main__':
    data = Solution().answer_1(
        [[1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100], [1, 100], [7, 100]]
    )

    print(data)
