"""
    给你一个字符串 s 和一个字符串列表 words ，你需要将在字符串列表中出现过的s的子串添加加粗闭合标签<b>和</b>。如果两个子串有重叠部分，你需要
把它们一起用一对闭合标签包围起来。同理，如果两个子字符串连续被加粗，那么你也需要把它们合起来用一对加粗标签包围。返回添加加粗标签后的字符串s。


    示例 1：
        输入： s = "abcxyz123", words = ["abc","123"]
        输出："<b>abc</b>xyz<b>123</b>"

    示例 2：
        输入：s = "aaabbcc", words = ["aaa","aab","bc"]
        输出："<b>aaabbc</b>c"

    提示：
        1 <= s.length <= 1000
        0 <= words.length <= 100
        1 <= words[i].length <= 1000
        s 和 words[i] 由英文字母和数字组成
        words 中的所有值 互不相同

"""
from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        return self.answer_1(s, words)

    def answer_1(self, s, words):
        s_len = len(s)
        mask = [False for i in range(s_len)]

        for index in range(s_len):
            for word in words:
                word_len = len(word)
                if s[index: word_len + index] == word:
                    for j in range(index, index + word_len):
                        mask[j] = True

        res = []

        for index in range(s_len):
            if mask[index] and (index == 0 or not mask[index - 1]):
                res.append("<b>")
            res.append(s[index])
            if mask[index] and (index == s_len - 1 or not mask[index + 1]):
                res.append("</b>")

        return "".join(res)
