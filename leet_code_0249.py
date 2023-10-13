"""
    给定一个字符串，对该字符串可以进行 “移位” 的操作，也就是将字符串中每个字母都变为其在字母表中后续的字母，比如："abc" -> "bcd"。这样我们
可以持续进行 “移位” 操作，从而生成如下移位序列：
    "abc" -> "bcd" -> ... -> "xyz"
    给定一个包含仅小写字母字符串的列表，将该列表中所有满足 “移位” 操作规律的组合进行分组并返回。



示例：

输入：["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
输出：
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
解释：可以认为字母表首尾相接，所以 'z' 的后续为 'a'，所以 ["az","ba"] 也满足 “移位” 操作规律。

"""
import collections
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        return self.answer_1(strings)

    def answer_1(self, strings):
        storage = collections.defaultdict(list)

        for word in strings:
            key = self._get_word_key(word)
            storage[key].append(word)
        return list(storage.values())

    @classmethod
    def _get_word_key(cls, word):
        word_len = len(word)

        if word_len == 1:
            return ""

        key = ""

        for index in range(word_len - 1):
            key_char = (ord(word[index + 1]) - ord(word[index]) + 26) % 26
            key += str(key_char) + ","
        return key


if __name__ == '__main__':
    data = Solution().answer_1(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z", "al"])
    print(data)
