#!/usr/bin/python3
"""https://leetcode.com/problems/valid-anagram/description/
    BigO: O(n)
"""


class Solution(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return (False)

        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        for c in t:
            if c in count:
                count[c] -= 1
            else:
                return (False)

        for cnt in count.values():
            if cnt != 0:
                return (False)

        return (True)

leetcode = Solution()
s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

print(leetcode.isAnagram(s1, t1))
print(leetcode.isAnagram(s2, t2))
