class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle:
            return 0
        elif len(needle) > len(haystack):
            return -1
        
        start = 0
        end = len(needle)
        
        while end <= len(haystack):
            if haystack[start:end] == needle:
                return start
            
            start += 1
            end += 1
            
        return -1