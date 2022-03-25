class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        new = []
        count = 0
    
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                new.append(0)
                count += 1
            elif nums[i] > nums[i-1]:
                new.append(1)
                count += 1
            else:
                count += 1
                new.append(-1)
                
        while 0 in new:
            new.remove(0)
            count -= 1

        if nums[0] > nums[1]:
            new.insert(0, 1)
            count += 1
        elif nums[0] < nums[1]:
            new.insert(0, -1)
            count += 1
        else:
            count += 1
            new.insert(0, 0)
        
        i = 1
        while i < count:
            if new[i] == new[i-1]:
                new.pop(i)
                count -= 1
            else:
                i += 1
        
        return count