# https://leetcode.com/problems/reverse-linked-list


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head: ListNode) -> Optional[ListNode]:
    if head.next is None:
        return head
    prev = head
    next = head.next
    head.next = None
    reverseLinkedList(next)
    head.next = prev


def printLinkedList(head: ListNode):
    temp = head
    while True:
        print(temp.val, end=" -> ")
        if temp.next is None:
            break
        temp = temp.next


lst = list(map(int, input("Enter nodes list: ").split()))
head = ListNode(lst[0])
temp = head
for el in lst[1:]:
    temp.next = ListNode(el)
    temp = temp.next

print("Given linked list:")
printLinkedList(head)
print("Reversed list:")
rev = reverseLinkedList(head)
# printLinkedList(head)

if rev:
    printLinkedList(head)
else:
    print("Reversed list not found")
