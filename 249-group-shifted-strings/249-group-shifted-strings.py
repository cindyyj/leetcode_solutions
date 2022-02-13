class Solution:
    def groupStrings(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for s in strs:
            key = tuple((ord(c) - ord(s[0])) % 26 for c in s) 
            groups[key].append(s)
        return groups.values()