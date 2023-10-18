"""
    给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。
    实现 MovingAverage 类：
        MovingAverage(int size) 用窗口大小 size 初始化对象。
        double next(int val) 计算并返回数据流中最后 size 个值的移动平均值。


    示例：
        输入：
            ["MovingAverage", "next", "next", "next", "next"]
            [[3], [1], [10], [3], [5]]
        输出：
            [null, 1.0, 5.5, 4.66667, 6.0]

        解释：
            MovingAverage movingAverage = new MovingAverage(3);
            movingAverage.next(1); // 返回 1.0 = 1 / 1
            movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
            movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
            movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3
"""
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self._size = size
        self._sum = 0
        self._queue = deque([])

    def next(self, val: int) -> float:
        queue_size = len(self._queue)
        if queue_size >= self._size:
            self._sum -= self._queue.popleft()
        self._queue.append(val)
        self._sum += val
        return self._sum / len(self._queue)


if __name__ == '__main__':
    a = MovingAverage(10).next(10)
