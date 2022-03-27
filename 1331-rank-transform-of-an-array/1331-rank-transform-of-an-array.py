class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        d = {num : i + 1 for i, num in enumerate(sorted(set(arr)))}
        return [d[num] for num in arr]
        # return list(map(d.get, arr))