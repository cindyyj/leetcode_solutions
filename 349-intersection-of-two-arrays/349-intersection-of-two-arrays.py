class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums1 or not nums2:
            return None
        
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)
        
        n1, n2 = sorted(nums1), sorted(nums2)
        p1 = p2 = 0 
        res = []
        
        while p1 < len(n1) and p2 < len(n2):
            if n1[p1] == n2[p2]:
                if n1[p1] not in res:
                    res.append(n1[p1])
                p1 += 1
                p2 += 1
            elif n1[p1] < n2[p2]:
                p1 += 1
            else:
                p2 += 1
        
        return res
        
        
#         # https://leetcode.com/problems/intersection-of-two-arrays/solution/
#         # return list(set(nums1) & set(nums2))
        
# #         This is a Facebook interview question.
# #         They ask for the intersection, which has a trivial solution using a hash or a set.

# #         Then they ask you to solve it under these constraints:
# #         O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
# #         You are told the lists are sorted.

# #         Cases to take into consideration include:
# #         duplicates, negative values, single value lists, 0's, and empty list arguments.
# #         Other considerations might include sparse arrays. 
        
#         nums1.sort()
#         nums2.sort()
#         length1, length2 = len(nums1), len(nums2)
#         intersection = list()
#         index1 = index2 = 0
#         while index1 < length1 and index2 < length2:
#             num1 = nums1[index1]
#             num2 = nums2[index2]
#             if num1 == num2:
#                 # 保证加入元素的唯一性
#                 if not intersection or num1 != intersection[-1]:
#                     intersection.append(num1)
#                 index1 += 1
#                 index2 += 1
#             elif num1 < num2:
#                 index1 += 1
#             else:
#                 index2 += 1
#         return intersection