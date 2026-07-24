class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next


def input_ll():
    arr = list(map(int, input("Enter list: ").split()))
    head = ListNode(arr[0])
    temp = head
    for el in arr[1:]:
        temp.next = ListNode(el)
        temp = temp.next
    return head


def print_ll(head: ListNode | None):
    if head:
        while head:
            print(head.val, end=", ")
            head = head.next
    print()
