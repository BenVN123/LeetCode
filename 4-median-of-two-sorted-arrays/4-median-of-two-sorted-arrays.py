class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        
        if len(nums1) % 2 != 0:
            return nums1[int((len(nums1)-1)/2)]

        return ((nums1[int((((len(nums1)-1)/2)+0.5))] + nums1[int((((len(nums1)-1)/2)-0.5))]))/2