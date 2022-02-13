class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if sorted(nums1) != sorted(nums2):
            return False
        
        return [nums2.index(num) for num in nums1]