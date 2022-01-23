class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = collections.Counter(s)
        c_t = collections.Counter(t)
        return c_s == c_t
