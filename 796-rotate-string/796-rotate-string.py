class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
#         # https://leetcode.com/problems/rotate-string/solution/
#         # 4 solutions
        
#         # 1. Brute Force, Time O(N**2), Space: O(1)
#         if len(s) != len(goal):
#             return False
#         if len(s) == 0:
#             return True
        
#         for i in range(len(s)):
#             if all( s[(x + i) % len(s)] == goal[x] for x in range(len(goal))):
#                 return True
        
        # 2. Simple check
        # All rotations of A are contained in A+A. Thus, we can simply check whether B is a substring of A+A      
        return len(s) == len(goal) and goal in s + s
        
        # 3. rolling hash 
        # 4. KMP to read 
        # KMP use a dp table to calculate shift