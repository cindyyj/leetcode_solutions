class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, count in freq.items() if count == 1][0]
        return ans
       
        # # super slow solution
        # for num in nums:
        #     if nums.count(num) == 1:
        #         return num      