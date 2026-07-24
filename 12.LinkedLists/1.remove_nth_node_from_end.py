from ll_commons import ListNode, input_ll, print_ll


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next
        return dummy.next


head = input_ll()
n = int(input("Enter n: "))
head = Solution().removeNthFromEnd(head, n)
print_ll(head)
