# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    
    # first split by space so that we have all commands as a list of strings
    commands = S.split(' ')
    
    stack = []

    for command in commands:

        if command == 'POP':

            if not stack:
                return -1
            stack.pop()

        elif command == 'DUP':

            if not stack:
                return -1
            stack.append(stack[-1])

        elif command == '+':

            if len(stack) < 2:
                return -1

            elem1 = stack.pop()
            elem2 = stack.pop()

            # if result is an overflow
            if elem1 + elem2 > 1048575:
                return -1

            stack.append(elem1 + elem2)
            
        elif command == '-':

            if len(stack) < 2:
                return -1

            elem1 = stack.pop()
            elem2 = stack.pop()

            if elem1 - elem2 < 0:
                return -1
            stack.append(elem1 - elem2)

        else:
            stack.append(int(command))

    if not stack:
        return -1
    
    return stack[-1]