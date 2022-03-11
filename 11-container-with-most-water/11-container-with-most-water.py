class Solution:
    def maxArea(self, height: List[int]) -> int:
        out = 0
        left, right = 0, len(height) - 1
        
        while right > left:
            out = max(out, min(height[left], height[right]) * (right - left))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return out