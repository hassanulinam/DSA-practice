"""https://leetcode.com/problems/add-two-numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list."""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional["ListNode"] = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional["ListNode"], l2: Optional["ListNode"]
    ) -> Optional["ListNode"]:
        ans = ListNode(0)
        dummy = ans
        carry = 0

        while l1 or l2 or carry:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            sm = a + b + carry
            dummy.next = ListNode(sm % 10)
            dummy = dummy.next
            carry = sm // 10

        return ans.next
