class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
        
        # 1-line, combinations r-length tuples, in sorted order, no repeated elements
        # combinations_with_replacement(r-length tuples, in sorted order, with repeated elements)
        from itertools import combinations
        return list(combinations(range(1, n+1), k))
        
