class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = 0
        
        for i in s[::-1]:
            if i != ' ':
                out += 1
            elif out > 0:
                break
            
        return out