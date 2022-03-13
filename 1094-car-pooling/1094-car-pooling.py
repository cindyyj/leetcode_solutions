class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)
        
        for num, start, end in trips:
            d[start] += num
            d[end] -= num
        
        maxp = 0
        total = 0
        for dist in sorted(d.keys()):
            total += d[dist]
            d[dist] = total
            maxp = max(d[dist], maxp)
        
        return maxp <= capacity