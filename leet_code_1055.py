"""
    对于任何字符串，我们可以通过删除其中一些字符（也可能不删除）来构造该字符串的 子序列 。(例如，“ace” 是 “abcde” 的子序列，而 “aec” 不是)。
给定源字符串 source 和目标字符串 target，返回 源字符串 source 中能通过串联形成目标字符串 target 的 子序列 的最小数量 。如果无法通过串联源
字符串中的子序列来构造目标字符串，则返回 -1。

    示例 1：
        输入：source = "abc", target = "abcbc"
        输出：2
        解释：目标字符串 "abcbc" 可以由 "abc" 和 "bc" 形成，它们都是源字符串 "abc" 的子序列。

    示例 2：
        输入：source = "abc", target = "acdbc"
        输出：-1
        解释：由于目标字符串中包含字符 "d"，所以无法由源字符串的子序列构建目标字符串。

    示例 3：
        输入：source = "xyz", target = "xzyxz"
        输出：3
        解释：目标字符串可以按如下方式构建： "xz" + "y" + "xz"。
"""


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        return self.answer_1(source, target)

    def answer_1(self, source, target):
        """
        当且仅当 target 的所有字符都存在于 source 中时，才能实现任务
        :param source:
        :param target:
        :return:
        """

        def _check_subsequence(to_check, in_string):
            """
            检查 to_check 是否是 in_string的子序列
            :param to_check:
            :param in_string:
            :return:
            """
            to_check_len, in_string_len = len(to_check), len(in_string)
            to_check_index = in_string_index = 0

            while to_check_index < to_check_len and in_string_index < in_string_len:
                if to_check[to_check_index] == in_string[in_string_index]:
                    to_check_index += 1
                in_string_index += 1
            return to_check_index == to_check_len

        source_chars = set(source)

        for target_char in target:
            if target_char not in source_chars:
                return -1

        new_source = source

        count = 1

        while not _check_subsequence(target, new_source):
            new_source += source
            count += 1

        return count
