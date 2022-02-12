from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # fruits[i] is the type of fruit the ith tree produces! not the number of fruits! 
        # longest subsequence that have 2 distinct types
        # pick one fruit from tree, --> maximum subarray length = max fruits
        # Longest Substring with at most 2 distinct characters
        
        maxl = 0
        start = 0
        d = defaultdict(int)
        
        for end, fruit in enumerate(fruits):
            d[fruit] += 1
            
            if len(d) > 2:
                d[fruits[start]] -= 1
                if d[fruits[start]] == 0:
                    del d[fruits[start]]
                start += 1
            
            maxl = max(maxl, end - start + 1)
        
        return maxl