# https://leetcode.com/problems/swap-nodes-in-pairs
from typing import Optional

from ll_commons import ListNode, input_ll, print_ll


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n1 = head
        n2 = head.next
        n3 = None
        if n2.next:
            n2.next = self.swapPairs(n2.next)
            n3 = n2.next

        n1.next = n3
        n2.next = n1
        return n2


head = input_ll()
head = Solution().swapPairs(head)
print_ll(head)
