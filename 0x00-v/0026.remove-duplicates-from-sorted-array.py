#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# BigO: O(n)
# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        
        index = 1
        for i in range(1, len(nums)):
            if (nums[i] != nums[i - 1]):
                nums[index] = nums[i]
                index += 1
        return (index)
# @lc code=end

