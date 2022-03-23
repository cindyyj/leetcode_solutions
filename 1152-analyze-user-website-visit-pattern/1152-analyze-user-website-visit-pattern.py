from collections import defaultdict
from itertools import combinations
# r-length tuples, in sorted order, no repeated elements
# All the combination of list in sorted order(without replacement) 

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        d = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            d[u].append(w)
        
        cnt = Counter()
        for sites in d.values():
            combs = set(combinations(sites, 3))
            for comb in combs:
                cnt[comb] += 1
        
        ans = sorted(cnt, key=lambda x : (-cnt[x], x))
        return ans[0]
        # return max(sorted(cnt), key=cnt.get)