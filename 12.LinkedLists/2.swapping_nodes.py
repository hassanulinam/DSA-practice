"""Return the head of the linked list after swapping the values
of the kth node from the beginning and the kth node from the end (the list is 1-indexed)."""

from typing import Optional

from ll_commons import ListNode, input_ll, print_ll


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(k):
            fast = fast.next
        curr = fast

        while fast:
            fast, slow = fast.next, slow.next

        curr.val, slow.val = slow.val, curr.val
        return dummy.next


head = input_ll()
k = int(input("Enter K: "))
head = Solution().swapNodes(head, k)
print_ll(head)
