class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        e = 0
        for i in nums:
            if i != e:
                return e
            e += 1
        
        return e