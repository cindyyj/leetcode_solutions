class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # converting every binary string to integer representation and adding to set
        # nums.length needs to be smaller than 16, so that able to convert to decimal number 
        # The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
        
        maxlen = len(nums[0])
        ans = (set(range(2**maxlen)) - set([int(i, 2) for i in nums])).pop()  # any of the possible answer, pop one
        return bin(ans)[2:].zfill(maxlen)       
        
#         s = set([int(i, 2) for i in nums])
#         maxlen = len(nums[0])
        
#         for i in range(pow(2, maxlen)):
#             if i not in s:
#                 r = bin(i)[2:]  # '0b1' stripping the first 2 letter 0b                
#                 return '0'*(maxlen - len(r)) + r #add back leading 0s! 