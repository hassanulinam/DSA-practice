# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

from typing import Optional

from ll_commons import ListNode, input_ll, print_ll


class Solution:
    def deleteDuplicates(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        return dummy.next


myll = input_ll()
print_ll(Solution().deleteDuplicates(myll))
