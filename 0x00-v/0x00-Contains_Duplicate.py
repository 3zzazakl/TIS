#!/usr/bin/python3
"""https://leetcode.com/problems/contains-duplicate/description/
    BigO: O(n)
"""


class Solution(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num = set()
        for i in nums:
            if i in num:
                return (True)
            num.add(i)
        return False


leetcode = Solution()
input1 = [1, 2, 3, 1]
input2 = [1, 2, 3, 4]
input3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(leetcode.containsDuplicate(input1))
print(leetcode.containsDuplicate(input2))
print(leetcode.containsDuplicate(input3))
