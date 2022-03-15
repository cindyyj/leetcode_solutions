class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        #  follow-up question from Google: what if the words are sorted lexicographically?
        
        return sum(w.startswith(pref) for w in words)
        
        # return sum(w.find(pref) == 0 for w in words)
        
#         cnt = 0
#         for w in words:
#             if w.startswith(pref):
#                 cnt += 1
        
#         return cnt            