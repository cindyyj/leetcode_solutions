class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # binary search
        # https://leetcode.com/problems/find-smallest-letter-greater-than-target/discuss/1568523/Python-easy-solution-with-detail-explanation-(modified-binary-search)
        # if the number is out of bound
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        low = 0
        high = len(letters)-1
        while low <= high:
            mid = (high+low)//2
            
            if  target >= letters[mid]: # in binary search this would be only greater than
                low = mid+1
            
            if target < letters[mid]:
                high = mid-1
                
        return letters[low]
    
#         # binary search, right boundary
        
#         l, r = 0, len(letters)-1
#         while l <= r:
#             mid = l + (r-l) // 2
#             if letters[mid] <= target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
        
#         if r < 0 or l >= len(letters):
#             return letters[0]
#         else:
#             return letters[l]
            
#         # https://leetcode.com/problems/find-smallest-letter-greater-than-target/solution/
#         for c in letters:
#             if c > target:
#                 return c
#         return letters[0]
        