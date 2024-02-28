#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# BigO = O(n)
# @lc code=start
class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        mChar = {}
        mWord = {}

        for char, word in zip(pattern, words):
            if char not in mChar:
                if word not in mWord or mWord[word] != char:
                    return False

                mChar[char] = word
                mWord[word] = char
            else:
                if mChar[char] != word:
                    return False
        return True
# @lc code=end
