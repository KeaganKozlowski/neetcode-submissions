class Solution:
    def isValid(self, s: str) -> bool:
        order, stack, ops = {']':'[', '}':'{', ')':'('}, [], 0
        for e in s:
            if e == '(' or e == '{' or e == '[':
                stack.append(e)
            elif len(stack) > 0:
                if stack[-1] == order[e]:
                    stack.pop()
                    ops += 2
        return True if ops == len(s) else False
        
        