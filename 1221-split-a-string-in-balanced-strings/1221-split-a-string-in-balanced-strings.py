class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = cnt = 0
        
        for char in s:
            cnt += 1 if char == 'R' else -1
            if cnt == 0:
                ans += 1
        
        return ans
        
        
# from itertools import accumulate

# class Solution:
#     def balancedStringSplit(self, s: str) -> int:
#         return list(accumulate(1 if c == "R" else -1 for c in s)).count(0)        

"""
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
"""