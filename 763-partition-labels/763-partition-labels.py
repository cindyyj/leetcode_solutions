class Solution:
    def partitionLabels(self, s: str) -> List[int]:
# Figure out the rightmost index first and use it to denote the start of the next section.
# Reset the left pointer at the start of each new section.
# Store the difference of right and left pointers + 1 as in the result for each section.

        last = {char : i for i, char in enumerate(s)} # last[char] -> index of S where char occurs last
        	
        left, right = 0, 0
        result = []
        
        for i, char in enumerate(s):
            right = max(right, last[char])
            
            if i == right:
                result += [right - left + 1]
                left = i + 1
        
        return result