class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        # bitmask
        mask = n
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        
        return n ^ mask
        
        
#         """
#         Time Complexity: O(1), since we're doing not more than 32 iterations here.
#         Space Complexity: O(1).
#         """
#         if n == 0:
#             return 1
#         todo, bit = n, 1
#         while todo:
#             # flip current bit
#             n ^= bit
#             bit <<= 1
#             todo >>= 1
#         return n
        