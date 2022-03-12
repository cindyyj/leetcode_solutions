class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        left, right, count = {}, {}, defaultdict(int)
        
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] += 1
        
        
        ans = len(nums)
        degree = max(count.values())
        
        for num in count:
            if count[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)
        
        return ans