class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lols = {']': '[', '}': '{', ')': '('}
        
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == lols[i]:
                    stack.pop(-1)
                else:
                    return False
        
        if len(stack) == 0:
            
            return True
        
        return False