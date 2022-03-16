class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        groups = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))
        
        
        # # itertools.groupby
        # groups = [len(list(v)) for _, v in itertools.groupby(s)]
        # return sum(min(a,b) for a, b in zip(groups, groups[1:]))