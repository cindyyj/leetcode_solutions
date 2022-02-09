class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n, spare, min_spare, min_idx = len(gas), 0, float('inf'), 0
        
        for i in range(n):
            spare += gas[i] - cost[i]  # total spare
            if spare < min_spare:
                min_spare = spare
                min_idx = i 
            
        return -1 if spare < 0 else (min_idx + 1) % n
        