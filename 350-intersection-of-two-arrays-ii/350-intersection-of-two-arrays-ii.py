class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # simple counter
        from collections import Counter
        return list((Counter(nums1) & Counter(nums2)).elements())

        
#         # two pointers
#         if not nums1 or not nums2:
#             return None
        
#         if len(nums1) > len(nums2):
#             return self.intersect(nums2, nums1)
        
#         res = list()
#         n1, n2 = sorted(nums1), sorted(nums2)
#         p1 = p2 = 0
        
#         while p1 < len(nums1) and p2 < len(nums2):
#             if n1[p1] == n2[p2]:
#                 res.append(n1[p1])
#                 p1 += 1
#                 p2 += 1
#             elif n1[p1] < n2[p2]:
#                 p1 += 1
#             else:
#                 p2 += 1
        
#         return res
        
        # https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247/Three-Python-Solutions
        # see the comments!!!