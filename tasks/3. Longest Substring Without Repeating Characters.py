"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = lon = 0
        hmap = {}
        for j in range(0, len(s)):
            if s[j] in hmap:
                i = max(i, hmap[s[j]] + 1)
            hmap[s[j]] = j
            lon = max(lon, j-i+1)
        return lon
