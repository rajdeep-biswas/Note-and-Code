# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # I found I have already solved this problem on June 2022 (I have no idea why I was Leetcoding in June 22)
    # Trying to read it, looks like I am doing multiple passes
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # The first pass is to count the number of nodes on the list. note that i improved the readability of this
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1

        # The second pass to traverse until we get to the (n + 1)th element, because 0-indexing?
        # so either n is the same as the length of the list or lesser, whichever we reach first, that is the element we need to get rid of
        temp = head
        while temp and count > n + 1: # count starts from the length of array reduces to n + 1; which is the node *before* the one we want to get rid of
            temp = temp.next
            count -= 1 # Counting down to know when to stop

        # this is probably where that edge cases comes in. maybe a list of length 1 or 2
        if count == n:
            head = head.next
        elif temp.next:
            temp.next = temp.next.next

        return head