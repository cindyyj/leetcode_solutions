class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # citations[i] >= n - i
        # H-index is n - i (n - i) paper cited at least c times
        
        n = len(citations)
        l, r = 0, n - 1
        
        while l <= r:
            mid = l + ((r - l) >> 1)
            
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
            
            # We didn't find an exact match, so there's exactly (n - left) papers that have citations
            # greater than or equal to citations[left] and that is our answer            
        return n - l
        
        # return sum(i < c for i, c in enumerate(citations[::-1]))