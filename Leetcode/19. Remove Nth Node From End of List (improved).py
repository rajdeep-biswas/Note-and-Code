# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # now this isn't exactly one-pass but a two-pass solution and it uses a dummy node, which might be inelegant (youtube.com/watch?v=XVuQxVej6y8)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # dummy node points to the head of Node. this only takes care of edge cases where the list size is 1
        # two pointer approach - left points at dummy and right points, for now, at head
        dummy = ListNode(0, head)
        left = dummy
        right = head
        count = 0

        # we want right to get a head start on left by a gap of n. (note just usign n + 1 and getting rid of dummy node works too but it fails the edge cases where list size is 1)
        while right and count < n:
            right = right.next
            count += 1

        # move both pointers to the right until 'right' hits null and hence left is positioned correctly *before* the element we want to get rid of
        while right:
            left = left.next
            right = right.next

        # simple operation of removing next element of left
        left.next = left.next.next

        # return the head node which is next of dummy (again, this returns null in case of we started with a single element list)
        return dummy.next