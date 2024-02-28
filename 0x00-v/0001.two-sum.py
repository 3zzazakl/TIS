#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# BigO = O(n)
# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        num = {}

        for i, ii in enumerate(nums):
            complement = target - ii
            if complement in num:
                return [num[complement], i]
            num[ii] = i
        return []
# @lc code=end

