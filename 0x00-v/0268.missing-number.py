#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# BigO = O(n)
# @lc code=start
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

# @lc code=end

