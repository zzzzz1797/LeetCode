"""
    给你一个字符串 S，找出所有长度为 K 且不含重复字符的子串，请你返回全部满足要求的子串的 数目。

    示例 1：
        输入：S = "havefunonleetcode", K = 5
        输出：6
        解释：
        这里有 6 个满足题意的子串，分别是：'havef','avefu','vefun','efuno','etcod','tcode'。

    示例 2：
        输入：S = "home", K = 5
        输出：0
        解释：
        注意：K 可能会大于 S 的长度。在这种情况下，就无法找到任何长度为 K 的子串。


    提示：
        1 <= S.length <= 10^4
        S 中的所有字符均为小写英文字母
        1 <= K <= 10^4
"""
import collections


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        return self.answer_1(s, k)

    def answer_1(self, s, k):
        s_len = len(s)

        if s_len < k:
            return 0

        left = right = result = 0

        counter = collections.defaultdict(int)

        while right < s_len:
            right_num = s[right]
            counter[right_num] += 1

            while counter[right_num] == 2:
                left_num = s[left]
                counter[left_num] -= 1
                if counter[left_num] == 0:
                    del counter[left_num]
                left += 1

            if len(counter) >= k:
                result += 1

            right += 1

        return result
