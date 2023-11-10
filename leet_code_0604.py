"""
    设计并实现一个迭代压缩字符串的数据结构。给定的压缩字符串的形式是，每个字母后面紧跟一个正整数，表示该字母在原始未压缩字符串中出现的次数。
设计一个数据结构，它支持如下两种操作： next 和 hasNext。
    next() - 如果原始字符串中仍有未压缩字符，则返回下一个字符，否则返回空格。
    hasNext() - 如果原始字符串中存在未压缩的的字母，则返回true，否则返回false。


    示例 1：
        输入：
            ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
            [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
        输出：
            [null, "L", "e", "e", "t", "C", "o", true, "d", true]

        解释：
            StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
            stringIterator.next(); // 返回 "L"
            stringIterator.next(); // 返回 "e"
            stringIterator.next(); // 返回 "e"
            stringIterator.next(); // 返回 "t"
            stringIterator.next(); // 返回 "C"
            stringIterator.next(); // 返回 "o"
            stringIterator.hasNext(); // 返回 True
            stringIterator.next(); // 返回 "d"
            stringIterator.hasNext(); // 返回 True
"""


class StringIterator:
    num_flag = set("0123456789")

    def __init__(self, compressedString: str):
        self._mappers = self._expand(compressedString)

    def _expand(self, s):
        length = len(s)
        index = 1

        last_char = s[0]
        result = []

        while index < length:
            total_cnt = ""
            while index < length and s[index] in self.num_flag:
                total_cnt += s[index]
                index += 1
            total_cnt = int(total_cnt) if total_cnt else 1

            result.append([last_char, total_cnt])
            if index >= length:
                break
            last_char = s[index]

            self._merge(result)
            index += 1

        self._merge(result)
        return list(reversed(result))

    @classmethod
    def _merge(cls, result):
        if len(result) <= 1:
            return
        if result[-1][0] == result[-2][0]:
            result[-2][1] += result[-1][1]
            result.pop()

    def next(self) -> str:
        if not self._mappers:
            return " "

        ans = self._mappers[-1][0]
        self._mappers[-1][1] -= 1
        if not self._mappers[-1][1]:
            self._mappers.pop()
        return ans

    def hasNext(self) -> bool:
        return bool(len(self._mappers))


if __name__ == '__main__':
    a = StringIterator("X15D18V8")
    for i in range(41):
        print(a.next())
    print(1111)
