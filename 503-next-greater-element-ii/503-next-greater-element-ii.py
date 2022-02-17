class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/next-greater-element-ii/solution/
        # 一个朴素的思想是，我们可以把这个循环数组「拉直」，即复制该序列的前 n-1n−1 个元素拼接在原序列的后面。这样我们就可以将这个新序列当作普通序列，用上文的方法来处理。
        
        n = len(nums)
        ans = [-1] * n
        stack = []
        
        for i in range(2*n - 1):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                ans[idx] = nums[i % n]
            stack.append(i % n)
        
        return ans
        
        
#         # brute force
#         res = [None]*len(nums)
        
#         for i in range(len(nums)):
#             is_greater = False
#             res[i] = -1
            
#             for j in range(len(nums)):
#                 if nums[i] < nums[j]:
#                     is_greater = True
#                     res[i] = nums[j]
#                     break

#         return res