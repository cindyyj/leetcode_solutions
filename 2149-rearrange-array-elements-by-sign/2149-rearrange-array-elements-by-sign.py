class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        
        ans = []
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        
        return ans