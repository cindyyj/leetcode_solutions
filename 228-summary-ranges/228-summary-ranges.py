class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for num in nums:
            if res and res[-1][1] == num - 1:
                res[-1][1] = num
            else:
                res.append([num, num])
        
        return [str(x) + "->" + str(y) if x != y else str(x) for x, y in res]        