class Solution:
    def maxPower(self, s: str) -> int:

        # Time Complexity: O(n) - solved by keeping track of last visited character and 2 counters (1 global, 1 local)
        # Space Complexity: O(1)

        prev_char = None
        max_power = 0
        local_power = 0
        
        for curr_char in s:
            if curr_char != prev_char:
                local_power = 1
            else: 
                local_power += 1 
            
            max_power = max(max_power, local_power)
            
            prev_char = curr_char
        
        return max_power