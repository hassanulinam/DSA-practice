# https://leetcode.com/problems/reverse-linked-list


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head: ListNode) -> tuple[ListNode, ListNode]:
    if head.next is None:
        return (head, head)
    next = head.next
    head.next = None
    reversed, last_node = reverseLinkedList(next)
    reversed.next = head
    return head, last_node


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
print("\nReversed list:")
_, rev = reverseLinkedList(head)
# printLinkedList(head)

if rev:
    printLinkedList(rev)
else:
    print("Reversed list not found")
