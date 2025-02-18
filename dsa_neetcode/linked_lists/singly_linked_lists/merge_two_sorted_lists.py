from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()  # handles edge case of inserting into an empty list

        while list1 and list2:  # while list 1 and 2 are not empty/null
            if list1.val < list2.val:
                node.next = list1  # add node to result output
                list1 = list1.next  # move on to next node in list1
            else:
                node.next = list2
                list2 = list2.next
            node = node.next  # move to next node in result output
            # (leaving dummy node behind)

        # if one of the lists is emtpy at this point, we want to take the list that is not empty
        # and append it to the result list
        node.next = list1 or list2

        return dummy.next  # new beginning of the list (because tail we kept incrementing but dummy never moved)
