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

        # intuitive solution with O(n) space using a hashmap to keep track of nodes and rewiring all of them in a single pass
        # will look at neetcode's solution that probably improves on this with O(1) space

        nodes = {}
        trav = head

        pos = 0
        while trav:
            nodes[pos] = trav
            trav = trav.next
            pos += 1

        i = 0
        j = len(nodes) - 1

        while i < j:
            nodes[i].next = nodes[j]
            nodes[j].next = nodes[i + 1]
            i += 1
            j -= 1

        # the last node needs to be next'd to null otherwise it creates a (self)-loop in the linked list
        nodes[i].next = None