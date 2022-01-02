class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashmap, time O(n), space O(n)
        
        hashdict = dict()
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hashdict:
                return [hashdict[complement]+1, i+1]
            hashdict[numbers[i]] = i
        
        return [-1, -1]
    
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
