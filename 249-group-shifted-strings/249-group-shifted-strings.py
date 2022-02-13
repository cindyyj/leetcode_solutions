class Solution:
    def groupStrings(self, strs: List[str]) -> List[List[str]]:
        
        # time: O(N*k), N = len(strs), k = max(len(s))
        # space: O(N*k)
        groups = defaultdict(list)
        for s in strs:
            key = tuple((ord(c) - ord(s[0])) % 26 for c in s)   # (a - z) -25 % 26 = 1 circular shift
            groups[key].append(s)
        return groups.values()