from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


# time complexity O(n)
# space complexity O(1)
def reverseListTwoPointer(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        nxt = curr.next  # store the link to the next node

        curr.next = prev  # reversing the link to the next node
        prev = curr  # shifting prev to current node

        curr = nxt  # shifting current node to next node to reverse
    return prev  # returning new head


# time complexity O(n)
# space complexity O(1)
def reverseListRecursively(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:  # base case
        return None

    new_head = head  # current node we are at with recursive call
    if head.next:  # "if there is still a sub-problem"
        new_head = self.reverseList(head.next)
        head.next.next = head  # reversing the link between the node in front and the current node
    head.next = None  # set the current nodes next node to null

    return new_head
