#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        left, right = 0, 0
        max_length = 0
        unique = set()

        while right < n:
            if s[right] not in unique:
                unique.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                unique.remove(s[left])
                left += 1
        return (max_length)
# @lc code=end

