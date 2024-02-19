#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# BigO: O(4^n/sqrt(n)
# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        result = []
        backtrack('', 0, 0)
        return result
# @lc code=end

