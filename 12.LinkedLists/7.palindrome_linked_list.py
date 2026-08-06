# https://leetcode.com/problems/palindrome-linked-list
from typing import Optional

from ll_commons import ListNode


class Solution:
    def isPalindrome(self, head: Optional["ListNode"]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        while prev:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next

        return True
