#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#
# BigO: O(n)
# @lc code=start
class Solution:
    def calPoints(self, operations):
        stack = []
        for op in operations:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
# @lc code=end

