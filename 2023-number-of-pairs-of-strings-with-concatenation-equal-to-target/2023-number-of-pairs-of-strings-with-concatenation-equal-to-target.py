class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # two sum with strings
        # brute force
        # return sum(i + j == target for i, j in permutations(nums, 2))
        # return sum(''.join(num_lst) == target for num_lst in permutations(nums, 2))
        
        
        # optimized with freq table
        freq = collections.Counter(nums)
        res = 0
        for k, v in freq.items():
            if target.startswith(k):
                suffix = target[len(k):]
                res += v * freq[suffix]
                
                if k == suffix:
                    res -= freq[suffix]
        return res
    
    """
special case when prefix == suffix:
I think it's better to think it this way. Using n strings you have to fill two positions _ _ . And number of possible ways to do so would be n for 1st position and remaining n - 1 for 2nd because we've already used one number for 1st pos and thus 2nd pos can be filled with remaining (n - 1) strings to form target.
And so according to multiplication principle -> n * (n - 1) should be the number of ways.
    """