"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2

Example 2:
Input: nums = [0,1]
Output: 2

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
"""


class Solution:
    def missing_umber(self, nums: list) -> int:
        etalon_nums = {i for i in range(len(nums) + 1)}
        not_etalon = set(nums)
        return etalon_nums.difference(not_etalon).pop()
