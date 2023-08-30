# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head.next

        while fast and fast.next:
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
            if slow.next:
                slow = slow.next

        # standard reversing the linkedlist
        prev = None
        cur = slow

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # prev is the head of the reversed 2nd half of the list and 'head' is still the original head
        left = head
        right = prev

        while left and right:
            leftnext = left.next
            rightnext = right.next

            left.next = right
            right.next = leftnext

            left = leftnext
            right = rightnext

        # PS: I understood Neetcode's solution and implemented it and it works. But I have no idea why my version works. For lists wth odd number of elements, the last element is supposed to get into a self-loop (I dry ran it twice) but running the code shows there are no cycles in the list. I am very confused