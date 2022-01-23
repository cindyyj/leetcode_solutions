class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one-line
        if len(s) != len(t):
            return False
        
        return collections.Counter(s) == collections.Counter(t)