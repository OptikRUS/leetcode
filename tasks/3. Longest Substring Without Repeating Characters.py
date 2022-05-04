"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = 0
        for i in range(len(s)):
            count = ''
            for j in range(i, len(s)):
                if s[j] not  in count:
                    count += s[j]
                    long = max(long, len(count))
                else:
                    break
        return long
