class Stack:
    # quick, rudimentary stack implementation since I already knew how to approach this problem.
    parens = []

    def __init__(self):
        self.parens = []

    def push(self, paren):
        self.parens.append(paren)

    def pop(self):
        return self.parens.pop()

class Solution:
    def isValid(self, s: str) -> bool:

        stk = Stack()

        # dictionary for simple checking of matching opening and closing parens.
        dic = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        check = True
        for letter in s:
            if letter in ['(', '[', '{']:
                # simply push into stack if it's one of the opening parens.
                stk.push(letter)

            if letter in [')', ']', '}']:
                # if the stack is empty when you encounter a closing paren, that right there is incorrect.
                # OR, if the last in element is popped and checked against the dictionary for a closing paren non-match, also incorrect. also, break right there for efficiency.
                if not stk.parens or dic[stk.pop()] != letter:
                    check = False
                    break

        # if anything is leftover in the stack that's incorrect.
        if stk.parens:
            return False
        return check