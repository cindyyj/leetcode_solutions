class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        # Linear-time Slice Using Substring + HashSet
        # much fast look up in set vs. in list
        # time & space, O((n-l)*l), n the loop executed N - L + 1 one builds a substring of length L. 
        
        # rabin-karp for multiple pattern search
        # Constant-time Slice Using Rolling Hash
        l, n = 10, len(s)
        seen, ans = set(), set()
        
        for start in range(n - l + 1):
            tmp = s[start : start + l]
            if tmp in seen:
                ans.add(tmp[:])
            seen.add(tmp)
        return ans        