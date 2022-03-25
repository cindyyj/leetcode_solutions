class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt1 = Counter(s1.split())
        cnt2 = Counter(s2.split())
        
        unique1 = [w for w in cnt1 if (cnt1[w] == 1 and cnt2[w] == 0)]
        unique2 = [w for w in cnt2 if (cnt2[w] == 1 and cnt1[w] == 0)]
        
        return unique1 + unique2