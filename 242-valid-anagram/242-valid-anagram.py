class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one-line
        return collections.Counter(s) == collections.Counter(t)
