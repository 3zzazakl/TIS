#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s, k):
        max_length, max_count, left = 0, 0, 0
        char_count = {}

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_count = max(max_count, char_count[s[right]])

            if ((right - left + 1 - max_count) > k):
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return (max_length)
# @lc code=end

