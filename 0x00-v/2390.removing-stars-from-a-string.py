#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#
# BigO = O(n)
# @lc code=start
class Solution:
    def removeStars(self, s):
        stack  = []

        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
# @lc code=end
