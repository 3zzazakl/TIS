#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
# BigO: O(n)
# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return (len(nums))

        index = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1
        return (index)
# @lc code=end
