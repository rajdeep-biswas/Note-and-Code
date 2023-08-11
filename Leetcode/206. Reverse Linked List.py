# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # even though this is an Easy problem,
        # but visually figuring out the exact sequence of step is super important, so this is gonna make it to the repo
        if not head or not head.next:
            return head

        prev = None
        cur = head

        while cur:

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev