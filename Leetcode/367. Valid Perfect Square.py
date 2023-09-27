class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # I was feeling I can't do iterative binary search so used this problem for validation; solution is pretty intuitive (once you recognize this is a binary search problem). start checking if num // 2 squares to num (reasonable start since this is perfect for num = 4), and then on look higher or lower and if our pointers run over each other that must mean it's not a perfect square and we return False

        l, r = 1, num

        while l <= r:

            m = (l + r) // 2

            if m ** 2 > num:
                r = m - 1
            
            elif m ** 2 < num:
                l = m + 1
            
            else:
                return True
        
        return False