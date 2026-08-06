# https://leetcode.com/problems/rotate-list

from typing import Optional

from ll_commons import ListNode, input_ll, print_ll


class Solution:
    def rotateRight(self, head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
        if not head or not k:
            return head
        total_len = 0
        temp = head
        while temp:
            temp = temp.next
            total_len += 1

        k = k % total_len
        slow = fast = head
        if k == 0:
            return head

        for i in range(k):
            if fast:
                fast = fast.next
            else:
                raise ValueError("Fast Pointer movement error. Check the k computation")
        if fast:
            fast = fast.next
        while fast and slow:
            fast, slow = fast.next, slow.next

        new_head = slow
        if slow:
            new_head = slow.next
            slow.next = None

        if new_head:
            new_head_end = new_head
            while new_head_end and new_head_end.next:
                new_head_end = new_head_end.next

            new_head_end.next = head

        return new_head


myll = input_ll()
k = int(input("Enter K: "))
print_ll(Solution().rotateRight(myll, k))
