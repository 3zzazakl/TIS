#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#
# BigO = O(n)
# @lc code=start
class Solution:
    def smallestNumber(self, pattern):
        n = len(pattern)
        result = []
        stack = []

        for i in range(n + 1):
            stack.append(i + 1)
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())
        return ''.join(map(str, result))
# @lc code=end
