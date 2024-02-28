#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# BigO = O(log n)
# @lc code=start
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
# @lc code=end

