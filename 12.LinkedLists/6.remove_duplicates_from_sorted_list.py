# https://leetcode.com/problems/remove-duplicates-from-sorted-list

from typing import Optional

from ll_commons import ListNode, input_ll, print_ll


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        temp = dummy.next
        last = head.val
        head = head.next
        while head:
            if head.val != last:
                temp.next = head
                temp = temp.next
                last = temp.val
            head = head.next
        temp.next = None
        return dummy.next


head = input_ll("Enter sorted list: ")
print_ll(Solution().deleteDuplicates(head))
