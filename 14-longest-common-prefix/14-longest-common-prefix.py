class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        out=''
        
        for i in range(len(strs[0])):
            for e in strs:
                try:
                    if e[i] != strs[0][i]:
                        return out
                except Exception:
                    return out
            out = strs[0][:i+1]
        
        return out