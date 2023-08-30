# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # I found I have already solved this problem on June 2022 (I have no idea why I was Leetcoding in June 22)
    # Trying to read it, looks like I am doing multiple passes
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # The first pass is to count the number of nodes on the list
        count = 1
        temp = head
        while temp.next:
            temp = temp.next
            count += 1

        # The second pass to traverse until we get to the (n + 1)th element, because 0-indexing?
        temp = head
        while temp.next and count > n + 1:
            temp = temp.next
            count -= 1 # I have no idea why I am counting down again, probably to get around some edge case

        # this is probably where that edge cases comes in. maybe a list of length 1 or 2
        if count == n:
            head = head.next
        elif temp.next:
            temp.next = temp.next.next

        return head