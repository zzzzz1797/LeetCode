"""
    给定一个表示单词列表的字符串 s 。单词中的每个字母都有一个或多个选项。

    如果有一个选项，则字母按原样表示。
    如果有多个选项，则用大括号分隔选项。例如,  "{a,b,c}"  表示选项  ["a", "b", "c"]  。
    例如，如果  s = "a{b,c}"  ，第一个字符总是 'a' ，但第二个字符可以是 'b' 或 'c' 。原来的列表是 ["ab", "ac"] 。

    请你 按字典顺序 ，返回所有以这种方式形成的单词。

    示例 1：
        输入：s = "{a,b}c{d,e}f"
        输出：["acdf","acef","bcdf","bcef"]

    示例 2：
        输入：s = "abcd"
        输出：["abcd"]
"""
from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        return self.answer_1(s)

    def answer_1(self, s):
        num, result = len(s), []

        def _backtrack(index, hold):
            if index == num:
                result.append("".join(hold))
                return

            if s[index] == "{":
                pre = index

                while s[index] != "}":
                    index += 1

                sub = s[pre + 1:index].split(",")

                for c in sub:
                    hold.append(c)
                    _backtrack(index + 1, hold)
                    hold.pop()
            else:
                hold.append(s[index])
                _backtrack(index + 1, hold)
                hold.pop()

        _backtrack(0, [])
        return sorted(result)
