class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
               
        nums = [lower-1] + nums + [upper+1]
        ans = []
        for lower, upper in zip(nums, nums[1:]):
            if lower + 2 == upper:
                ans.append(f"{lower + 1}")
            elif lower + 2 < upper:
                ans.append(f"{lower + 1}->{upper - 1}")
        return ans