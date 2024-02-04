#!/usr/bin/python3
"""https://leetcode.com/problems/happy-number/description/
    BigO:
"""


class Solution(object):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happy = set()

        while n != 1:
            n = sum(int(num) ** 2 for num in str(n))
            if n in happy:
                return (False)
            happy.add(n)
        return (True)


leetcode = Solution()
n1 = 19
n2 = 2

print(leetcode.isHappy(n1))
print(leetcode.isHappy(n2))
