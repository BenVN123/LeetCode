class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        
        i, length = 0, len(nums)
        while i < length:
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
            i+=1