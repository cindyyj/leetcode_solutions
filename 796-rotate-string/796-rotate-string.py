class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        # https://leetcode.com/problems/rotate-string/solution/
        # 4 solutions
        
        # Brute Force 
        if len(s) != len(goal):
            return False
        if len(s) == 0:
            return True
        
        for i in range(len(s)):
            if all( s[(x + i) % len(s)] == goal[x] for x in range(len(goal))):
                return True
        