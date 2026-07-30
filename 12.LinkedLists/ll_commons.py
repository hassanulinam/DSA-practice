class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode | None = next


def input_ll(msg="Enter list: "):
    arr = list(map(int, input(msg).split()))
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
