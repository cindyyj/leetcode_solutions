class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(map(int, nums))
        return str(nums[-k])
