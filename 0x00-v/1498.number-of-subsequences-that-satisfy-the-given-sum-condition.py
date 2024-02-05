#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#
# BigO: O(nlogn)
# @lc code=start
class Solution:
    def numSubseq(self, nums, target):
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        result = 0
        
        while left <= right:
            if (nums[left] + nums[right] <= target):
                result = (result + pow(2, right - left, mod)) % mod
                left += 1
            else:
                right -= 1
        return result
# @lc code=end
