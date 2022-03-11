class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []: return [-1,-1]
        
        lol = -1
        
        bruh = 0
        while bruh < len(nums):
            print(nums[bruh])
            if nums[bruh] == target:
                lol = bruh
                break
            elif nums[bruh] > target:
                return [-1, -1]
            bruh+=1
            
        bruh=len(nums)-1
        while bruh > lol - 1:
            if nums[bruh] == target:
                return [lol, bruh]
            bruh-=1
            
        return [-1,-1]