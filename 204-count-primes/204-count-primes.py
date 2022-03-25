class Solution:
    def countPrimes(self, n: int) -> int:
        lol = [0, 0] + [1] * (n - 1)
        
        for i in range(ceil(n**0.5) + 1):
            if lol[i]:
                for e in range(i*i, n+1, i):
                    lol[e] = 0
                    
        return sum(lol[:-1])