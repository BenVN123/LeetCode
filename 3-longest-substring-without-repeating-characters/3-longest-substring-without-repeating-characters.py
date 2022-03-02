class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '': return 0
        
        seen = set([s[0]])
        start, end, l = 0, 0, 1
        
        while end < len(s):
            if s[end] not in seen or start == end:
                seen.add(s[end])
                end += 1
            else:
                seen.remove(s[start])
                start += 1
                seen.add(s[start])
                            
            if (end - start)> l:
                l = end - start
                
        return l