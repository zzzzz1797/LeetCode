"""
    给你一个整数 n ，表示编号从 1 到 n 的 n 门课程。另给你一个数组 relations ，其中 relations[i] = [prevCoursei, nextCoursei] ，表
示课程 prevCoursei 和课程 nextCoursei 之间存在先修关系：课程 prevCoursei 必须在 nextCoursei 之前修读完成。
    在一个学期内，你可以学习 任意数量 的课程，但前提是你已经在上一学期修读完待学习课程的所有先修课程。
    请你返回学完全部课程所需的 最少 学期数。如果没有办法做到学完全部这些课程的话，就返回 -1。

    示例 1：
        输入：n = 3, relations = [[1,3],[2,3]]
        输出：2
        解释：
            在第一学期，可以修读课程 1 和 2 。
            在第二学期，可以修读课程 3 。

    示例 2：
        输入：n = 3, relations = [[1,2],[2,3],[3,1]]
        输出：-1
        解释：没有课程可以学习，因为它们互为先修课程。
"""
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        return self.answer_1(n, relations)

    def answer_1(self, n, relations):
        graph = {i: [] for i in range(1, n + 1)}

        for in_, out_ in relations:
            graph[in_].append(out_)

        for node in graph:
            if self._check_cycle(node, graph):
                return -1

        return max([self._get_max_length(i, graph) for i in graph])

    def _get_max_length(self, node, graph, flag=None):
        if flag is None:
            flag = {}

        if node in flag:
            return flag[node]

        max_length = 1
        for out_node in graph[node]:
            length = self._get_max_length(out_node, graph, flag)
            max_length = max(max_length, length + 1)
        flag[node] = max_length
        return max_length

    def _check_cycle(self, node, graph, flag=None):
        if flag is None:
            flag = {}

        if node in flag:
            return flag[node]

        flag[node] = True

        for out_node in graph[node]:
            if self._check_cycle(out_node, graph, flag):
                return True
        flag[node] = False
        return False


if __name__ == '__main__':
    Solution().minimumSemesters(3, [[1, 3], [2, 3]])
