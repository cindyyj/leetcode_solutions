from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # two pointers
        # time complexity O(ns), space O(1), k <= 26
        ns, np = len(s), len(p)
        if ns < np:
            return []
        
        countp = Counter(p)
        counts = Counter()
        
        res = []
        # sliding window on string s
        for i in range(ns):
            counts[s[i]] += 1
            
            if i >= np:
                counts[s[i - np]] -= 1
            
            if countp == counts:
                res.append(i - np + 1)
                
        return res
        
        
#         # not optimized solution!
#         if len(p) > len(s):
#             return []
        
#         countp = Counter(p)
        
#         res = []
#         for i in range( (len(s) - len(p) + 1)):
#             if countp == Counter(s[i : i + len(p)]):
#                 res.append(i)
        
#         return res