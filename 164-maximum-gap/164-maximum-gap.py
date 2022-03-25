class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        
        out = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > out:
                out = nums[i] - nums[i-1]
        return out