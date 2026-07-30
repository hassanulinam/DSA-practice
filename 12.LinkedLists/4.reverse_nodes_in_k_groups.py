# https://leetcode.com/problems/reverse-nodes-in-k-group
from typing import Optional

from ll_commons import ListNode, input_ll, print_ll


# WIP
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head
        n1 = head
        n2 = head.next
        n3 = None
        if n2.next:
            n2.next = self.reverseKGroup(n2.next, k - 1)
            n3 = n2.next

        n1.next = n3
        n2.next = n1
        return n2


head = input_ll()
k = int(input("Enter K: "))  # group size
head = Solution().reverseKGroup(head, k)
print_ll(head)
