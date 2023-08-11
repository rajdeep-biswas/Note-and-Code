# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # this is an easy problem but the simple idea of using a dummy node is just perfect
        dummy = ListNode(-1)
        dummy.next = head

        trav = dummy

        while trav:
            if trav.next and trav.next.val == val:
                trav.next = trav.next.next
            else:
                trav = trav.next
        
        return dummy.next