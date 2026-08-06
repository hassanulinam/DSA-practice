# https://leetcode.com/problems/rotate-list

from typing import Optional

from ll_commons import ListNode, input_ll, print_ll


class Solution:
    def rotateRight(self, head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
        if not head or not head.next or k == 0:
            return head
        n, tail = 1, head
        while tail and tail.next:
            tail = tail.next
            n += 1
        k %= n
        if k == 0:
            return head

        tail.next = head
        steps = n - k
        for _ in range(steps):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head


myll = input_ll()
k = int(input("Enter K: "))
print_ll(Solution().rotateRight(myll, k))
