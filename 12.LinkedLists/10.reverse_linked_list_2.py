# https://leetcode.com/problems/reverse-linked-list-ii

from typing import Optional

from ll_commons import ListNode, input_ll, print_ll


class Solution:
    def reverse(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if not head or not head.next:
            return head

        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rest

    def reverseBetween(
        self, head: Optional["ListNode"], left: int, right: int
    ) -> Optional["ListNode"]:
        if not head or not head.next or right - left <= 0:
            return head
        dummy = ListNode(0, head)
        prev_head = dummy
        for _ in range(left - 1):
            prev_head = prev_head.next

        cur = prev_head.next
        for i in range(right - left):
            middle = cur.next
            cur.next = middle.next
            middle.next = prev_head.next
            prev_head.next = middle

        return dummy.next


myll = input_ll()
left = int(input("Enter left: "))
right = int(input("Enter right: "))
print_ll(Solution().reverseBetween(myll, left, right))
