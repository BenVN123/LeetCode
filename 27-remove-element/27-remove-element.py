class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        while True:
            try:
                if nums[i] == val:
                    del nums[i]
                else:
                    i += 1
            except:
                break
                
        return len(nums)