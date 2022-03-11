class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums)-1
        
        while end-start > 0:
            mid = int((start+end)//2)
            
            if nums[mid] > target:
                end = mid-1
                
            elif nums[mid] < target:
                start = mid+1
                
            else: return mid
        
        if nums[start] < target:
            return start+1
        
        return start