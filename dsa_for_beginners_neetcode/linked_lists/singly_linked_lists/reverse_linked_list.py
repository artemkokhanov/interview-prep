# This is a two-pointer solution
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# iterative solution has time complexity O(n) and space complexity O(1)
class iterativeSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next  # store the link to the next node
            curr.next = prev  # reversing the link to the next node
            prev = curr  # shifting prev to current node
            curr = nxt  # shifting current node to next node to reverse
        return prev  # returning new head


# recursive solution has time complexity O(n) and space complexity O(1)
class recursiveSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # base case
            return None

        newHead = head  # current node we are at with recursive call
        if head.next:  # "if there is still a sub-problem"
            newHead = self.reverseList(head.next)
            head.next.next = head  # reversing the link between the next node and head
        head.next = None

        return newHead
