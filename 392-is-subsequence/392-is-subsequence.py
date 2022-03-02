class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        for i in t:
            if i == s[0]:
                if len(s) == 1:
                    return True
                s = s[1:]
            
            if len(s) == 0:
                return True
        
        return False
