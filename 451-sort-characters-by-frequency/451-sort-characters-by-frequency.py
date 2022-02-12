from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Strings are Immutable!
        counts = Counter(s)
        
        # rebuild the string
        res = []
        for char, freq in counts.most_common():
            res.append(char * freq)
        
        return ''.join(res)
        