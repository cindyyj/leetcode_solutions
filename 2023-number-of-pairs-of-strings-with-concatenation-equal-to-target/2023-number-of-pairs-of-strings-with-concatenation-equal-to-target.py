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