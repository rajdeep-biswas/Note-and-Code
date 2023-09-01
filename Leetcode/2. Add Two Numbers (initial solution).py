# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    """
    According to leetcode, this is my third sitting with this problem. I had the first session in June 2021 which has an accepted solution but hacky stuff like converting to a python list (clean af modularized code though, gotta give it that).
    The second sitting was in February 2022 where I have written this unreadable monstrosity solution that doesn't even work (1341 / 1568 testcases passed), I didn't even try to read it.
    This third attempt came pretty naturally to me; O(len(l1) + len(l2)) time and O(max(len(l1), len(l2))) space. Still gonna check out Neetcode's
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        travl1 = l1
        travl2 = l2

        # I hate dummy nodes but will just sail it
        res_dummy = ListNode(-1)
        travres = res_dummy

        carry = 0

        # While there are still elements in both lists
        while travl1 and travl2:

            # add the two different numbers along with any carry
            added = travl1.val + travl2.val + carry
            travres.next = ListNode(added % 10) # no conditionals necessary, if the result is 9 or below, %10-ing it will not affect it.
            carry = added // 10 # same comment as line 29

            travl1 = travl1.next
            travl2 = travl2.next
            travres = travres.next

        # do it for any remaining elements in L1
        while travl1:
            added = travl1.val + carry
            travres.next = ListNode(added % 10) # see comments on previous while block if this doesn't make sense
            carry = added // 10

            travl1 = travl1.next
            travres = travres.next

        # see comments on previous while block if this doesn't make sense
        while travl2:
            added = travl2.val + carry
            travres.next = ListNode(added % 10)
            carry = added // 10
            
            travl2 = travl2.next
            travres = travres.next

        # any leftover carry needs to be appended as another node to the list
        if carry:
            travres.next = ListNode(carry)
            carry //= 10 # this isn't even needed. just because I can

        return res_dummy.next # since the dummy in itself is useless