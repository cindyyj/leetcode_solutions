from collections import defaultdict
from itertools import combinations
# r-length tuples, in sorted order, no repeated elements
# All the combination of list in sorted order(without replacement) 
# .sort() method is only for lists and sorts by mutating the list in
# place; invoked using dot notation
# • sorted() function can be used to sort any sequence (strings, lists,
# tuples). It always returns a new sorted list, and does NOT modify
# the original sequence
# Sorting a list of (or a tuple of) tuples with sorted() sorts elements in
# ascending order by their first item
# • If there is a tie, Python breaks the tie by comparing the second items
# • If the second items are also tied, it compares the third items, and so on


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

        return list(min(cnt, key=lambda k: (-cnt[k], k))) 
    
        # ans = sorted(cnt, key=lambda x : (-cnt[x], x))  # sort descending by value, then lexicographically
        # return ans[0]
    
        # return max(sorted(cnt), key=cnt.get)