"""
    系统中存在 n 个进程，形成一个有根树结构。给你两个整数数组 pid 和 ppid ，其中 pid[i] 是第i个进程的 ID ，ppid[i]是第i个进程的父进程ID 。
每一个进程只有 一个父进程 ，但是可能会有一个或者多个子进程 。只有一个进程的 ppid[i] = 0 ，意味着这个进程 没有父进程 。

    当一个进程 被杀掉 的时候，它所有的子进程和后代进程都要被杀掉。

    给你一个整数 kill 表示要杀掉进程的 ID ，返回被杀掉的进程的 ID 列表。可以按 任意顺序 返回答案。

    示例 1：
        输入：pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
        输出：[5,10]
        解释：涂为红色的进程是应该被杀掉的进程。
"""
import collections
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        return self.answer_1(pid, ppid, kill)

    def answer_1(self, pids, ppids, kill):
        result = []

        if not kill:
            return result

        result.append(kill)

        for index, ppid in enumerate(ppids):
            if ppid == kill:
                result.extend(self.answer_1(pids, ppids, pids[index]))
        return result

    def answer_2(self, pids, ppids, kill):

        ppid_mapper = collections.defaultdict(list)

        for index, ppid in enumerate(ppids):
            ppid_mapper[ppid].append(pids[index])

        result = []

        def _dfs(i):
            result.append(i)

            for j in ppid_mapper[i]:
                _dfs(j)

        _dfs(kill)
        return result
