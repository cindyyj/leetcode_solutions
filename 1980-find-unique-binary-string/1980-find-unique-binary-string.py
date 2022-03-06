class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # converting every binary string to integer representation and adding to set
        # nums.length needs to be smaller than 16, so that able to convert to decimal number 
        
        s = set([int(i, 2) for i in nums])
        maxlen = len(nums[0])
        
        for i in range(pow(2, maxlen)):
            if i not in s:
                r = bin(i)[2:]  # '0b1' stripping the first 2 letter 0b                
                return '0'*(maxlen - len(r)) + r #add back leading 0s! 