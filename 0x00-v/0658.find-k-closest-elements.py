#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - 1

        while ((right - left + 1) > k):
            if (abs(arr[left] - x) > abs(arr[right] - x)):
                left += 1

            else:
                right -= 1
        return (arr[left:right + 1])
# @lc code=end

