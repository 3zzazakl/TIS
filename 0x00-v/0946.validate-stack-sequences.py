#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
# BigO = O(n)
# @lc code=start
class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        x = 0

        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[x]:
                stack.pop()
                x += 1
        return x == len(popped)
# @lc code=end

