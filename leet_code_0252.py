"""
    给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判断一个人是否能够
参加这里面的全部会议。

    示例 1：
        输入：intervals = [[0,30],[5,10],[15,20]]
        输出：false

    示例 2：
        输入：intervals = [[2,4],[3,8]]
        输出：true

    提示：
        0 <= intervals.length <= 104
        intervals[i].length == 2
        0 <= starti < endi <= 106
"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        return self.answer_1(intervals)

    def answer_1(self, intervals):
        intervals.sort()

        for index in range(1, len(intervals)):
            if intervals[index - 1][1] > intervals[index][0]:
                return False

        return True
