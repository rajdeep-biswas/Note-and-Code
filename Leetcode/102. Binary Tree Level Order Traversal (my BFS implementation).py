# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # BFS implementation with a tweak. inner loop captures same level elements in sub-lists instead of all elements going serially into a single list
    # Update: found out that my implementation is the exact same as Neetcode's. The only difference is that he uses collections.deque() with which the .popleft() method comes with O(1) time but .insert(0, n) on a regular list (which is what I am doing) is actually O(n) time since it needs to shift all elements to the right. added to TIL
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # corner case of empty array being passed in. since we're inserting into a queue that will be [None] and loop does execute and it's a whole can of worms to not include this test, so better leave this here
        if not root:
            return None
        
        # bfs is the 2D list that will contain the level order traversals and queue is our data structure needed for the bfs which is empty initially and by the end
        bfs = []
        queue = []

        # i could have just done queue = [root] but this is slightly more graceful and readable
        queue.insert(0, root)

        while queue:

            # populate a list of nodes to iterate it later
            # this is only needed because we need a 2D list as the result
            nodes = []
            while queue:
                popped = queue.pop()
                nodes.append(popped)

            # iterate each node at level, append current level's nodes to level list and insert all left and right children to queue
            level = []
            for node in nodes:

                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
                
                level.append(node.val)
            
            # append populated level list to main list
            bfs.append(level)
        
        return bfs