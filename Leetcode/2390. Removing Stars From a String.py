class Solution:
    def removeStars(self, s: str) -> str:

        # handpicked low effort problem to keep up streak
        # tbf it only seemed easy because I knew it was in the "stack" pattern. otherwise would have busted some more ass

        stack = []

        for letter in s:
            if letter == '*':
                stack.pop()
            else:
                stack.append(letter)
        
        return ''.join(stack)