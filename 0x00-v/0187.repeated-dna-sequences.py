#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        seq_set = set()
        repeated_seq = set()

        for i in range(len(s) - 9):
            current = s[i:i + 10]
            if (current in seq_set):
                repeated_seq.add(current)
            else:
                seq_set.add(current)
        return (list(repeated_seq))
# @lc code=end

