# https://leetcode.com/problems/merge-two-sorted-lists
from typing import Optional

from ll_commons import ListNode, input_ll, print_ll


class Solution:
    def mergeTwoLists(
        self, list1: Optional["ListNode"], list2: Optional["ListNode"]
    ) -> Optional["ListNode"]:
        dummy = ListNode(0)
        temp = dummy
        while list1 and list2:
            if list1.val < list2.val:
                temp.next, list1 = list1, list1.next
            else:
                temp.next, list2 = list2, list2.next
            temp = temp.next

        temp.next = list1 or list2
        return dummy.next


h1 = input_ll("Enter sorted list: ")
h2 = input_ll("Enter sorted list-2: ")
res = Solution().mergeTwoLists(h1, h2)
print_ll(res)
