class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        #  follow-up question from Google: what if the words are sorted lexicographically?
        # You can use binary search twice to locate the lower and upper bounds of the words that have the same prefix.
        # Therefore, the time cost is still O(klogn).
        # Assume perf = "abcd", we can search "abcd" and "abcda" respectively.
        
        return sum(w.startswith(pref) for w in words)
        
        # return sum(w.find(pref) == 0 for w in words)
        
#         cnt = 0
#         for w in words:
#             if w.startswith(pref):
#                 cnt += 1
        
#         return cnt            