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
        
        # in-place stratgy 
        l, r = 0, len(num) - 1
        while l <= r:
            
            # Clean Python3 solution.
            # dict.get(key) returns None if it cannot find they key's value in the dictionary. 
            # So we can directly compare that with any number and it will return False
            # if num[l] not in rotated_map or rotated_map[num[l]] != num[r]
            
            if rotated_map.get(num[l]) != num[r]:
                return False
            l += 1
            r -= 1
        
        return True
        
        # rebuild rotated string, time O(n), space O(n)
#         for char in reversed(num):
#             if char not in rotated_map:
#                 return False
#             rotated.append(rotated_map[char])
            
#         return num == ''.join(rotated)
        