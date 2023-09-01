"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    """
    I came up with a pretty inelegant solution that needs 3 different hashmaps to keep track of what connects to what, and has to traverse the 2 different lists a total of 5 separate times
    It *is* O(n) time so I am pretty happy with it but it's probably not ideal for interview contexts
    But I am indeed satisfied that I was able to come up with this solution
    I have also committed an image Leetcode/supplementary/138_hashmaps.png as a better presented doodle from when I was figuring it out on pen and paper
    """

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        # getting original positions
        # the dictionary original_position holds keys of Node class which each map to a value of their position (order of appearance) i.e. Node#1: 0, Node#2: 1, etc.

        original_position = {}
        trav = head
        position = 0

        while trav:
            original_position[trav] = position
            trav = trav.next
            position += 1


        # getting original random mapping; note that this isn't possible without populating the original_positions hashmap, so it does need a second iteration
        # the dictionary original_random holds keys of position (order of appearance) which each map to their random's order of appearance i.e. position(Node#1): position(Node#3) (Node#1's random points to Node#3), and a conditional takes care of any random pointer pointing to null on line 43. for a DBMS analogy this sort of serves as a "join table" which is connecting the "primary keys"

        original_random = {}
        trav = head
        position = 0

        while trav:
            original_random[position] = original_position[trav.random] if trav.random else None
            trav = trav.next
            position += 1


        # creating a deep copy of the basic linked list (without populating the random pointers yet)
        # standard copying procedure I've been using since I discovered #234 (https://github.com/rajdeep-biswas/Note-and-Code/blob/master/Leetcode/234.%20Palindrome%20Linked%20List.py)
        copy_head = Node(head.val)
        ctrav = copy_head
        trav = head

        while trav.next:
            ctrav.next = Node(trav.next.val)
            ctrav = ctrav.next
            trav = trav.next


        # running the equivalent of line 23 but for the copied linkedlist, and also inverted
        # the dictionary copy_position_inv holds keys of positions against values of the actual copied nodes. this along with original_random comes into play at the final while loop. this iteration can probably be merged with the one above, but I thought it was cleaner to keep the "while trav.next" logic separate
        copy_position_inv = {}
        ctrav = copy_head
        position = 0

        while ctrav:
            copy_position_inv[position] = ctrav
            ctrav = ctrav.next
            position += 1


        # traversing the copied array one final time to populate the random pointers to their designated values
        ctrav = copy_head
        position = 0

        while ctrav:
            # this refers to original_random hashmap to figure out which position's random points to which position,
            # and uses the index of the latter from copy_position_inv to point it to the right object
            # tedious but clever imo, gotta check out neetcode's solution
            ctrav.random = copy_position_inv[original_random[position]] if original_random[position] != None else None
            ctrav = ctrav.next
            position += 1

        return copy_head