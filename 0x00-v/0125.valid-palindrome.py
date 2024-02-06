#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# BigO: O(n)
# @lc code=start
class Solution:
    def isPalindrome(self, s):
        s = ''.join(filter(str.isalnum, s)).lower()
        return (s == s[::-1])
# @lc code=end  
