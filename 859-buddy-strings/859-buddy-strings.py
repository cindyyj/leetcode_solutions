class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """
        If A.length() != B.length(): no possible swap
        If A == B, we need swap two same characters. Check is duplicated char in A.
        In other cases, we find index for A[i] != B[i]. There should be only 2 diffs and it's our one swap.
        """
        
        if len(s) != len(goal):
            return False
        if len(s) < 2:
            return False
        
        if s == goal and len(set(s)) < len(s):
            return True
        
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]      