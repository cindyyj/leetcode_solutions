class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return None
        
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        # num1 always the shorter array 
        nums1.sort()
        nums2.sort()
        
        res = list()
        
        p1 = p2 = 0
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
                
        return res        