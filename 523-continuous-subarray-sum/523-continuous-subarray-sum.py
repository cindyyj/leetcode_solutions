class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        pres = list(accumulate(nums))
        d = defaultdict(int)
        d[0] = -1 
        
        for i, pre in enumerate(pres):
            key = pre % k
            if key in d and i - d[key] > 1:
                return True
            elif key not in d:  # save the leftmost index that key appears
                d[key] = i
                
        return False 