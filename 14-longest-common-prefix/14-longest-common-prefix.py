class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        return shortest
        
        
        # res = ""
        # for s in zip(*strs):
        #     if len(set(s)) == 1:
        #         res += s[0]
        #     else:
        #         break
        # return res        