class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        rotated_map = {
            '0' : '0',
            '1' : '1',
            '8' : '8',
            '6' : '9',
            '9' : '6'       
        }
        
        rotated = []
        for char in reversed(num):
            if char not in rotated_map:
                return False
            rotated.append(rotated_map[char])
            
        return num == ''.join(rotated)
        