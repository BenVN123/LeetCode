class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        
        if nums[-1] < 1:
            return 1
        elif nums[-1] == 1:
            return 2
        
        for i in range(0, len(nums)):
            if nums[i] > 0:
                supposed = [i for i in range(1, len(nums)+1)]
                nums = nums[i:]
                break
        
        for i in range(0, len(nums)):
            if nums[i] != supposed[i]:
                return supposed[i]
            
        return nums[-1] + 1