class Solution:
    def jump(self, nums: List[int]) -> int:
        length, curr, nxt, ans, i = len(nums) - 1, -1, 0, 0, 0
        
        while nxt < length:
            if i > curr:
                ans += 1
                curr = nxt
            nxt = max(nxt, i + nums[i])
            i += 1
            
        return ans