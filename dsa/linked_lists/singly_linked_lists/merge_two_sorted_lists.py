from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Handles edge case of inserting into an empty list:
        # Node is used to create the new linked list which is a merging of the two inputted linked lists
        # Think of node as a pointer on where to insert the next node in the merged list
        # Dummy is used in the return statement to get the beginning of the new list
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next  # at this point, we have left the dummy node behind and continued with the next element in the result

        # append the linked list that is still not empty
        node.next = list1 or list2

        return dummy.next  # new beginning of the list (because tail we kept incrementing but dummy never moved)
