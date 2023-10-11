"""
  给定一个数字 N，当它满足以下条件的时候返回 true：原数字旋转 180° 以后可以得到新的数字。 如 0, 1, 6, 8, 9 旋转 180° 以后，得到了新的数字
0, 1, 9, 8, 6 。 2, 3, 4, 5, 7 旋转 180° 后，得到的不是数字。 易混淆数 (confusing number) 在旋转180°以后，可以得到和原来不同的数，且
新数字的每一位都是有效的。
"""


class Solution:
    _NUM_MAPPER = {
        0: 0,
        1: 1,
        6: 9,
        9: 6,
        8: 8
    }

    def confusingNumber(self, n: int) -> bool:
        return self.answer_1(n)

    def answer_1(self, n):
        new_n = 0
        old_n = n

        while n:
            tmp_n = n % 10
            if tmp_n not in self._NUM_MAPPER:
                return False

            n = n // 10
            new_n = new_n * 10 + self._NUM_MAPPER[tmp_n]

        return new_n != old_n


if __name__ == '__main__':
    print(Solution().answer_1(6))
