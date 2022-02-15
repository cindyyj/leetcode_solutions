from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # c1 - c2 subtract (keeping only positive counts)
        # min steps to make t as s, change t
        return sum((Counter(s) - Counter(t)).values())