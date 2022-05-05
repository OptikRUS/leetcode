"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
https://leetcode.com/problems/add-two-numbers/
"""
# not complete

class Solution(object):
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        revrse_l1 = ''.join(list(map(str, l1)))[::-1]
        revrse_l2 = ''.join(list(map(str, l2)))[::-1]
        summ = int(revrse_l1) + int(revrse_l2)
        return list(str(summ)[::-1])


l1 = [2, 4, 3]
l2 = [5, 6, 4]
s = Solution()
print(s.add_two_numbers(l1, l2))
