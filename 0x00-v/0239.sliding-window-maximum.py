#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        dq = deque()

        for i in range(len(nums)):
            while (dq and dq[0] < (i - k + 1)):
                dq.popleft()

            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            if (i >= k - 1):
                result.append(nums[dq[0]])
        return (result)
# @lc code=end

