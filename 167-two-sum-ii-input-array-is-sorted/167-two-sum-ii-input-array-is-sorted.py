class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
#         # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search)
#         # two-pointer
#     def twoSum1(self, numbers, target):
#         l, r = 0, len(numbers)-1
#         while l < r:
#             s = numbers[l] + numbers[r]
#             if s == target:
#                 return [l+1, r+1]
#             elif s < target:
#                 l += 1
#             else:
#                 r -= 1

#     # dictionary           
#     def twoSum2(self, numbers, target):
#         dic = {}
#         for i, num in enumerate(numbers):
#             if target-num in dic:
#                 return [dic[target-num]+1, i+1]
#             dic[num] = i

#     # binary search        
#     def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1
                
#         # hashmap, time O(n), space O(n)
        
#         hashdict = dict()
#         for i in range(len(numbers)):
#             complement = target - numbers[i]
#             if complement in hashdict:
#                 return [hashdict[complement]+1, i+1]
#             hashdict[numbers[i]] = i
        
#         return [-1, -1]
    
#         # two pointer, time O(n), space O(1)
#         l, r = 0, len(numbers)-1

#         while l<r:
#             s = numbers[l] + numbers[r]
#             if s == target:
#                 return [l+1, r+1]
#             elif s < target:
#                 l += 1
#             else:
#                 r -= 1
#         return [-1, -1]
