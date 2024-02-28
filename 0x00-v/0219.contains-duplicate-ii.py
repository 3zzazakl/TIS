#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if ((k == 0) or len(nums) == 1):
            return (False)

        num = set()
        for i in range (len(nums)):
            if (i > k):
                num.remove(nums[i - k - 1])
            if (nums[i] in num):
                return (True)
            num.add(nums[i])

        return (False)
# @lc code=end

