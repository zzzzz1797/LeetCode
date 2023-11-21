"""
    新一轮的「力扣杯」编程大赛即将启动，为了动态显示参赛者的得分数据，需要设计一个排行榜 Leaderboard。
请你帮忙来设计这个 Leaderboard 类，使得它有如下 3 个函数：
    1. addScore(playerId, score)：
        假如参赛者已经在排行榜上，就给他的当前得分增加 score 点分值并更新排行。
        假如该参赛者不在排行榜上，就把他添加到榜单上，并且将分数设置为 score。

    2. top(K)：返回前 K 名参赛者的 得分总和。
    3. reset(playerId)：将指定参赛者的成绩清零（换句话说，将其从排行榜中删除）。题目保证在调用此函数前，该参赛者已有成绩，并且在榜单上。

    请注意，在初始状态下，排行榜是空的。


    示例 1：
        输入：
            ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
            [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
        输出：
            [null,null,null,null,null,null,73,null,null,null,141]

        解释：
            Leaderboard leaderboard = new Leaderboard ();
            leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
            leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
            leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
            leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
            leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
            leaderboard.top(1);           // returns 73;
            leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
            leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
            leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
            leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
https://leetcode.cn/problems/design-a-leaderboard
"""

import heapq
from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self._score_mapper = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self._score_mapper[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for v in self._score_mapper.values():
            heapq.heappush(heap, v)
            if len(heap) > K:
                heapq.heappop(heap)

        return sum(heap)

    def reset(self, playerId: int) -> None:
        self._score_mapper.pop(playerId, None)
