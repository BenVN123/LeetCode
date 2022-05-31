class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {"(":")", "{":"}", "[":"]"}
        
        for i in s:
            stack.append(i)
            
            try:
                if len(stack) == 1:
                    continue
                elif i == closers[stack[-2]]:
                    stack = stack[:-2]
            except KeyError:
                return False
                    
        return len(stack) == 0