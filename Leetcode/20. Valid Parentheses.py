class Solution:
    def isValid(self, s):
        stack = []
        
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif (len(stack) != 0 and stack[-1] == '(' and ch == ')') or (len(stack) != 0 and stack[-1] == '{' and ch == '}') or (len(stack) != 0 and stack[-1] == '[' and ch == ']'):
                stack.pop()
            else:
                return False                  

        if len(stack) != 0:
            return False
        else:
            return True
