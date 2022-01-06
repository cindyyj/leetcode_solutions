class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 由于我们目标是找到某个数其在 nums2nums2 的右边中第一个比其大的数，因此我们可以对 nums2nums2 进行逆序遍历。
        # 我们在遍历 nums2nums2 时，实时维护一个单调栈，
        # 当我们遍历到元素 nums2[i]nums2[i] 时，可以先将栈顶中比 nums2[i]nums2[i] 小的元素出栈，最终结果有两种可能：
        # 栈为空，说明 nums2[i]nums2[i] 之前（右边）没有比其大的数；
        # 栈不为空， 此时栈顶元素为 nums2[i]nums2[i] 在 nums2nums2 中（右边）最近的比其大的数

        res = {}
        stack = []
        
        for num in reversed(nums2):
            # for every element, if top of stack smaller, then pop out
            # keep largest element (on the right) in stack
            while stack and num >= stack[-1]:
                stack.pop()
            
            # if empty stack
            res[num] = stack[-1] if stack else -1
            
            stack.append(num)
        
        return[res[num] for num in nums1]
        
#         # Brute Force, T O(mn), S: O(1)
#         res = []
#         for i in range(len(nums1)):
            
#             j = nums2.index(nums1[i])
            
#             is_greater = False
#             for element in nums2[j:]:
#                 if element > nums1[i]:
#                     is_greater = True
#                     res.append(element)
#                     break
            
#             if not is_greater:
#                 res.append(-1)
            
#         return res