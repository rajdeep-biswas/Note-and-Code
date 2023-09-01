# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # note that the same solution with O(n) space and O(n) time, but much easier, can be achieved by simply creating a normal list and reversing that instead of making a copy of the entire linkedlist
    # but since web searches have a distinct lack of an intuitive linkedlist deep copy solution (which I got by questioning ChatGPT a bunch), I chose to put this up on my repo
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # taking backup of the original linkedlist, making a deep copy of a linked list is way harder than it comes off as
        # committing this solution to my repo solely to take note of lines 11 to 18
        backup = ListNode(head.val)
        btrav = backup
        trav = head

        while trav.next:
            btrav.next = ListNode(trav.next.val)
            btrav = btrav.next
            trav = trav.next

        # standard reversing the linkedlist
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # comparing original list with reversed list...
        trav = prev # note that prev is now 'head'
        btrav = backup

        while trav and btrav:

            # ... element by element
            if trav.val != btrav.val:
                return False
            trav = trav.next
            btrav = btrav.next

        return True