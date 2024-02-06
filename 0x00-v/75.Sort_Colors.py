#!/usr/bin/python3
"""https://leetcode.com/problems/sort-colors/description/
    BigO: O(n)
"""


class Solution(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while (mid <= high):
            if (nums[mid] == 0):
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1


leetcode = Solution()
nums1 = [2, 0, 2, 1, 1, 0]
nums2 = [2, 0, 1]

leetcode.sortColors(nums1)
leetcode.sortColors(nums2)

print(nums1)
print(nums2)
