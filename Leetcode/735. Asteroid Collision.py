class Solution:

    # my hacky improvement over neetcode's hacky solution
    # line 33 has the explanation of why I think it's hacky

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for astr in asteroids:

            # stack[-1] is astl
            while stack and stack[-1] > 0 and astr < 0:

                astl = stack.pop()

                # if astl survives
                if abs(astl) > abs(astr):
                    # put it back in stack
                    stack.append(astl)
                    # and don't add astl since it's dead
                    astr = 0

                # if none survive, don't have to put astl back in                    
                elif abs(astl) == abs(astr):
                    # also, don't and astl since it's dead
                    astr = 0
                
                # else astr survives and astl dies
                # don't put astl back in and also, do put in astr outside of the loop
            
            # this is the hacky part. this only executes either if stack is empty (always on the first iteration) or if stack gets totally empty
            # in all other cases astr is set to 0 in the inner loop so that this line does not execute. also no astroid has a value of 0, so that fact is exploited at the while condition
            if astr:
                stack.append(astr)
        
        return stack