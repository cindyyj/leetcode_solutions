class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # two pointer
        n, m = len(s), len(t)
        if n > m:
            return False
        
        i, j = 0, 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n
        
""" 
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/is-subsequence/solution/pan-duan-zi-xu-lie-by-leetcode-solution/
"""