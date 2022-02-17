class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        cnt = Counter(s)
        ans = []
        
        for c in order:
            ans.extend( c * cnt[c] )
            del cnt[c] # or cnt[c] = 0
            
        for c in cnt:
            ans.extend( c * cnt[c] )
        
        return "".join(ans)