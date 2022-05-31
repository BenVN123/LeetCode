class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {"(":")", "{":"}", "[":"]"}
        
        for i in s:
            if i in closers.keys():
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif closers[stack[-1]] == i:
                stack = stack[:-1]
            else:
                return False
                
        return len(stack) == 0