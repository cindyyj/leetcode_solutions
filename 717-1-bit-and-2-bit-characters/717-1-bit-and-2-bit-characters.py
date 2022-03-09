class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        pos = 0
        while pos < len(bits) - 1:
            if bits[pos] == 1:
                pos += 2
            else:
                pos += 1
        
        return pos == len(bits) - 1
        
        