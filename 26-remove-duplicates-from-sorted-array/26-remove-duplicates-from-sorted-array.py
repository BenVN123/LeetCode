class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp, length, i = None, 0, 0
        
        while True:
            try:
                if nums[i] != tmp:
                    length += 1
                    tmp = nums[i]
                    i+=1
                else:
                    nums.pop(i)
            except Exception: break
            
        return length