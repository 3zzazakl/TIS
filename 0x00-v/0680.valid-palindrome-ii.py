#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# BigO: O(n)
# @lc code=start
class Solution:
    def validPalindrome(self, s):
        def isPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return (False)
                left += 1
                right -= 1
            return (True)

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return (isPalindrome(s, left + 1, right) or isPalindrome(s, left, right - 1))
            left += 1
            right -= 1
        return (True)
# @lc code=end

