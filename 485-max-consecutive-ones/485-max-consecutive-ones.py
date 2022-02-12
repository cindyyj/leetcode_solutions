class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # # fancy one liner solution as shared by Stefan Pochmann.
        # return max(list(map(len, ''.join(map(str, nums)).split('0') )))
        
        maxlen = l = 0

        for num in nums:
            if num == 1:
                l += 1
                maxlen = max(maxlen, l)
            else:           
                l = 0
                
        return maxlen