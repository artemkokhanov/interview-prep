from typing import Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


# https://youtu.be/G0_I-ZF0S38

# time complexity O(n)
# space complexity O(1)
def reverseListIterativelyTwoPointer(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:  # make sure current node is not None
        nxt = curr.nxt  # store the link to the next node

        curr.nxt = prev  # reversing the link to the next node
        prev = curr  # shifting prev to current node

        curr = nxt  # shifting current node to next node to reverse
    return prev  # returning new head


# time complexity O(n)
# space complexity O(1)
def reverseListRecursively(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:  # base case
        return None

    new_head = head  # current node we are at with recursive call
    if head.next:  # "if there is still a sub-problem"
        new_head = reverseListRecursively(head.next)
        head.next.next = head  # reversing the link between the node in front and the current node
    head.next = None  # set the current nodes next node to null

    return new_head
