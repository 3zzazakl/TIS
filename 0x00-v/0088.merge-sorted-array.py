#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# BigO = O(m + n) #
# @lc code=start
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        ii = n - 1
        iii = m + n - 1
        
        while i >= 0 and ii >= 0:
            if nums1[i] > nums2[ii]:
                nums1[iii] = nums1[i]
                i -= 1
            else:
                nums1[iii] = nums2[ii]
                ii -= 1
            iii -= 1
        
        while ii >= 0:
            nums1[iii] = nums2[ii]
            ii -= 1
            iii -= 1
# @lc code=end

