"""
    假设你是一个专业的狗仔，参加了一个 n 人派对，其中每个人被从 0 到n-1标号。在这个派对人群当中可能存在一位 “名人”。所谓 “名人” 的定义是：其
他所有 n - 1 个人都认识他/她，而他/她并不认识其他任何人。
    现在你想要确认这个 “名人” 是谁，或者确定这里没有 “名人”。而你唯一能做的就是问诸如 “A 你好呀，请问你认不认识 B呀？” 的问题，以确定A是否认
识 B。你需要在（渐近意义上）尽可能少的问题内来确定这位 “名人” 是谁（或者确定这里没有 “名人”）。

    在本题中，你可以使用辅助函数 bool knows(a, b) 获取到 A 是否认识 B。请你来实现一个函数 int findCelebrity(n)。
    派对最多只会有一个 “名人” 参加。若 “名人” 存在，请返回他/她的编号；若 “名人” 不存在，请返回 -1。
"""


def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        return self.answer_1(n)

    def answer_1(self, n):
        for i in range(n):
            if self._is_celebrity(i, n):
                return i
        return -1

    def _is_celebrity(self, i, count):
        for index in range(count):
            if index == i:
                continue
            if not (not knows(i, index) and knows(index, i)):
                return False
        return True
