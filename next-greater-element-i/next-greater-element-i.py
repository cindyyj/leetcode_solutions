class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums1)):
            
            j = nums2.index(nums1[i])
            
            is_greater = False
            for element in nums2[j:]:
                if element > nums1[i]:
                    is_greater = True
                    res.append(element)
                    break
            
            if not is_greater:
                res.append(-1)
            
        return res