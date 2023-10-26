"""
    给定有向图的边edges，以及该图的始点source和目标终点 destination，确定从始点source出发的所有路径是否最终结束于目标终点destination，即：
        从始点 source 到目标终点 destination 存在至少一条路径
        如果存在从始点 source 到没有出边的节点的路径，则该节点就是路径终点。
        从始点source到目标终点 destination 可能路径数是有限数字
    当从始点 source 出发的所有路径都可以到达目标终点 destination 时返回 true，否则返回 false。

    示例 1：
        输入：n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
        输出：false
        说明：节点 1 和节点 2 都可以到达，但也会卡在那里。

    示例 2：
        输入：n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
        输出：false
        说明：有两种可能：在节点 3 处结束，或是在节点 1 和节点 2 之间无限循环。

    示例 3：
        输入：n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
        输出：true
"""
from collections import defaultdict
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        return self.answer_1(n, edges, source, destination)

    def answer_1(self, n, edges, source, destination):
        graph = defaultdict(list)
        depended = defaultdict(int)

        for in_, out_ in edges:
            graph[out_].append(in_)
            depended[in_] += 1

        if depended[destination]:
            return False

        for i in range(n):
            if i != destination and depended[i] == 0:
                depended[i] += 1

        def dfs(u):
            if u == source:
                return True

            for v in graph[u]:
                depended[v] -= 1
                if not depended[v]:
                    if dfs(v):
                        return True
            return False

        return dfs(destination)
