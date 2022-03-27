class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # two sum with strings
        
        return sum(''.join(num_lst) == target for num_lst in permutations(nums, 2))
        