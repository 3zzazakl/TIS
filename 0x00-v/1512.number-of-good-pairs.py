#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#
# BigO = O(n)
# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums):
        count = {}
        pairs = 0

        for i in nums:
            if i in count:
                pairs += count[i]
                count[i] += 1
            else:
                count[i] = 1
        return pairs
# @lc code=end
