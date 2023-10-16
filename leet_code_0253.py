"""
    给你一个会议时间安排的数组intervals，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回 所需会议室的最小数量。


    示例 1：
        输入：intervals = [[0,30],[5,10],[15,20]]
        输出：2

    示例 2：
        输入：intervals = [[7,10],[2,4]]
        输出：1


    提示：
        1 <= intervals.length <= 104
        0 <= starti < endi <= 106
"""
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return self.answer_1(intervals)

    def answer_1(self, intervals):
        events = []

        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1], -1))

        events.sort()

        result, tmp = float("-inf"), 0

        for _, flag in events:
            tmp += flag
            result = max(result, tmp)
        return result
