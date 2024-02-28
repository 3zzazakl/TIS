#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# BigO = O(logn)
# @lc code=start
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
# @lc code=end

