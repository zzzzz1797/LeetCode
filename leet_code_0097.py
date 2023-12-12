"""
    给定三个字符串s1、s2、s3，请你帮忙验证s3是否是由s1和s2交错组成的。两个字符串s和t交错的定义与过程如下，其中每个字符串都会被分割成若干非空
子字符串：
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
    注意：a + b 意味着字符串 a 和 b 连接。


    示例 1：
        输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        输出：true

    示例 2：
        输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
        输出：false

    示例 3：
        输入：s1 = "", s2 = "", s3 = ""
        输出：true

https://leetcode.cn/problems/interleaving-string/description/
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.answer_1(s1, s2, s3)

    def answer_1(self, s1, s2, s3):
        """
            dp[i][j] 表示 s1 的前i个字符串 和 s2的前j个字符串是否能构成s3的前i+j个字符串
            dp[0][0] 一定是true
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3:
            return False

        dp = [[False] * (len2 + 1) for i in range(len1 + 1)]
        dp[0][0] = True

        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, len2 + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                    dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                )

        return dp[-1][-1]
