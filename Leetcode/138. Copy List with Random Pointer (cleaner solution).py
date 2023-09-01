"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    # turns out my idea wasn't very different from Neetcode's. he was just cleverer with his hashmap usage. both our solutions are O(n) in both space and time
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        node_hash = {} # PS: it can be pretty elegant to initialize as node_hash = {None: None} if you want to avoid the conditional at line 44

        # first iteration / pass through the list to create a basic deep copy (just with the values and nexts, ignoring the randoms since some random pointers might point to nodes that haven't been populated yet)
        copy_head = Node(head.val)
        ctrav = copy_head
        trav = head

        while trav.next:
            ctrav.next = Node(trav.next.val)

            node_hash[trav] = ctrav # the idea is to create a hashmap of nodes that have old node keys against new node values

            ctrav = ctrav.next
            trav = trav.next

        # add the remaining pair to the hashmap since we went by trav.next condition on the while loop and not just "while trav"
        node_hash[trav] = ctrav


        # second pass to wire the randoms together now that we know where to look based on the hashmap
        ctrav = copy_head
        trav = head

        while ctrav:

            # trav.random points to just another node that already exists (or just points to null). once you take the node_hash value of it, it gives you the copied node (value) that is mapped from the original (key); these map 1:1 in terms of position. Go through my original solution Leetcode/138. Copy List with Random Pointer (intial hashmapy-heavy solution).py and the supplementary illustration PNG to get a better idea of what's going on. Over there, I had done a similar thing - with more steps.
            ctrav.random = node_hash[trav.random] if trav.random != None else None # the random pointer is totally free to point at null (think of the bit that is being pointed to, by the last node), so this conditional is necessary

            ctrav = ctrav.next
            trav = trav.next
        
        return copy_head