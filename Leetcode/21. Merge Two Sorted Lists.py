# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # take supplementary empty node and keep a backup
        head = newL = ListNode()

        # iterate as long as both the list pointers are non-null (lists are not empty yet)
        while list1 and list2:

            # compare pairs of list items' values and attach it to head node list and advance either list's pointer
            if list1.val <= list2.val:
                newL.next = list1
                list1 = list1.next
            elif list2:
                newL.next = list2
                list2 = list2.next

            # advance head node's pointer in order to pick next smallest element
            newL = newL.next

        # attach any remaining list to the end of head node
        if list1:
            newL.next = list1
        if list2:
            newL.next = list2

        # return list from head's next since head is an empty node
        return head.next