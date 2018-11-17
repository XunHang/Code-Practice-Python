'''
You are given two non-empty linked lists representing two
non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two
numbers and return it as a linked list.

You may assume the two numbers do not contain any leading
zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 自己定义一套加法，注意进位就好~
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        if (l1.val + l2.val) > 9:
            lr = ListNode(l1.val + l2.val - 10)
            carry = 1
        else:
            lr = ListNode(l1.val + l2.val)
        lr_buffer = lr
        l1 = l1.next
        l2 = l2.next
        while (l1 is not None and l2 is not None):
            if (l1.val + l2.val + carry) > 9:
                lr.next = ListNode(l1.val + l2.val + carry - 10)
                lr = lr.next
                carry = 1
            else:
                lr.next = ListNode(l1.val + l2.val + carry)
                lr = lr.next
                carry = 0
            l1 = l1.next
            l2 = l2.next

        while (l1 is not None):
            if (l1.val + carry) > 9:
                lr.next = ListNode(l1.val + carry - 10)
                carry = 1
                lr = lr.next
            else:
                lr.next = ListNode(l1.val + carry)
                carry = 0
                lr = lr.next
            l1 = l1.next
        while (l2 is not None):
            if (l2.val + carry) > 9:
                lr.next = ListNode(l2.val + carry - 10)
                carry = 1
                lr = lr.next
            else:
                lr.next = ListNode(l2.val + carry)
                carry = 0
                lr = lr.next
            l2 = l2.next

        if carry == 1:
            lr.next = ListNode(1)

        return lr_buffer


slt = Solution()

l1 = ListNode(2)
l1_1 = ListNode(4)
l1_2 = ListNode(3)
l1.next = l1_1
l1_1.next = l1_2
l2 = ListNode(5)
l2_1 = ListNode(6)
l2_2 = ListNode(4)
l2.next = l2_1
l2_1.next = l2_2
result = slt.addTwoNumbers(l1, l2)

print(result.val, result.next.val, result.next.next.val)
