class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out = digits
        out[-1] += 1
        
        for i in range(len(out))[::-1]:
            if out[i] == 10:
                out[i] = 0
                if i > 0:
                    out[i-1] += 1
                else:
                    out.insert(0, 1)

        return out