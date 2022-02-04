class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
# # --------------------------- METHOD 1 ---------------------------    
#         # Simply overwrite the end of the first list(nums1) with the second list(nums2), and then sort nums1.
#         # Python's built in sort method is a spin off of merge sort called Timsort, more information here - https://en.wikipedia.org/wiki/Timsort.
#         # It's essentially no better or worse than merge sort, which means that its run time on average is O(n log n) and its space complexity is Ω(n)
#         nums1[m:] = nums2
#         nums1.sort()
        
        
# --------------------------- METHOD 2 ---------------------------        
        # two pointers 1 , Time & Space: O(m+n)
        i = j = 0
        res = []
        
        while i < m or j < n:
            if i == m:
                res.extend(nums2[j:])
                break
            elif j == n:
                res.extend(nums1[i:m])
                break
            elif nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
                
        # change nums1 in place
        nums1[:] = res

        
#         # two pointer backwards, Time O(m+n), Space O(1) modify in place
#         pointer1 = m-1
#         pointer2 = n-1
#         write_index = m+n-1
        
#         while pointer2 >= 0:
#             if pointer1 >=0 and nums1[pointer1] > nums2[pointer2]:
#                 nums1[write_index] = nums1[pointer1]
#                 pointer1 -= 1
#             else:
#                 nums1[write_index] = nums2[pointer2]
#                 pointer2 -= 1
        
#             write_index -= 1 