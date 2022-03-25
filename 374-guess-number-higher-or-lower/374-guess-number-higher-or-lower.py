# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def f(start,end):
            g=guess((start+end)//2)
            if guess(start)==0:return start
            if guess(end)==0:return end
            if g==0:return (start+end)//2
            if g==1:return f((start+end)//2,end)
            if g==-1:return f(start,(start+end)//2)
        return f(0,n)
        