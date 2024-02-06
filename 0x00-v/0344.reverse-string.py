#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# BigO: O(n)
# @lc code=start
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
# @lc code=end

