"""
    给定一个 无重复元素 的整数数组 preorder ， 如果它是以二叉搜索树的先序遍历排列 ，返回 true 。

    示例 1：
        输入: preorder = [5,2,1,3,6]
        输出: true

    示例 2：
        输入: preorder = [5,2,6,1,3]
        输出: false

"""
from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        return self.answer_1(preorder)

    def answer_1(self, preorder):
        """
        如果出现递减序列，则是左子树，否则是右子树；
        右子树一定是递增的
        """

        stack = []
        min_value = float("-inf")

        for index in range(len(preorder)):
            if preorder[index] < min_value:
                return False

            while stack and preorder[index] > stack[-1]:
                min_value = stack.pop()
            stack.append(preorder[index])
        return True
