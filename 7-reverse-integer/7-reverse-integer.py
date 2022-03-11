class Solution:
    def reverse(self, x: int) -> int:
        e = ''
        
        if len(str(x)) < 2:
            return x
        
        for i in range(len(str(x))-1, -1, -1):
            e += str(x)[i]
            
        if e[0] == '0':
            e = e[1:]
            
        if len(e) > 1:
            if e[-1] == '-':
                e = e[0:-1]
                e = -1*int(e)
        
        if int(e) < -2147483648 or int(e) > 2147483647: return 0
        
        return int(e)