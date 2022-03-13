class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        d = defaultdict(int)
        for born, died in logs:
            for year in range(born, died):
                d[year] += 1
        
        max_alive = 0
        res = 0
        for year in range(1950, 2051):
            alive = d[year]
            if alive > max_alive:
                res = year
                max_alive = alive
            
        return res