"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
https://leetcode.com/problems/add-two-numbers/
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = int(self.unpack_list_node(l1)) + int(self.unpack_list_node(l2))
        if result:
            return self.pack_list_node(result)
        return ListNode(0)

    @staticmethod
    def unpack_list_node(ln):
        count = str(ln.val)
        seq = ln.next
        while seq:
            count += str(seq.val)
            seq = seq.next
        return count

    @staticmethod
    def pack_list_node(num, total_nodes=[]):
        for i in str(num):
            total_nodes.append(ListNode(int(i)))
        for j in range(len(total_nodes) - 1):
            total_nodes[j+1].next = total_nodes[j]
        return total_nodes[-1]

#
# l1 = ListNode(9, ListNode(4, ListNode(2)))
# l2 = ListNode(9, ListNode(4, ListNode(6, ListNode(5))))
# la = ListNode(8, ListNode(0, ListNode(7)))


# s = Solution()
# print(s.add_two_numbers(l1, l2))
# print(s.add_two_numbers(l1, l2).val)
# print(s.add_two_numbers(l1, l2).next.val)
# print(s.add_two_numbers(l1, l2).next.next.val)
# print(s.add_two_numbers(l1, l2).next.next.next.val)
# print(s.add_two_numbers(l1, l2).next.next.next.next.val)


# def pack_list_node(num, total_nodes=[]):
#     for i in str(num):
#         total_nodes.append(ListNode(int(i)))
#     for j in range(len(total_nodes) - 1):
#         total_nodes[j+1].next = total_nodes[j]
#     return total_nodes[-1]


# s = pack_list_node(10407)
# print(s.val)
# print(s.next.val)
# print(s.next.next.val)
# print(s.next.next.next.val)
# print(s.next.next.next.next.val)


# print(l1.next.val)
# print(l1.next.next.val)

# node_3 = ListNode(3)
# node_2 = ListNode(4)
# node_1 = ListNode(2)
# node_1.next = node_2
# node_2.next = node_3


# print(la)
# print(la.val)
# print(la.next.val)
# print(la.next.next.val)

# @staticmethod
# def unpack_list_node(ln):
#     arr = [ln.val]
#     seq = ln.next
#     while seq:
#         arr.append(seq.val)
#         seq = seq.next
#     return arr

