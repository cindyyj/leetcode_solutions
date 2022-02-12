class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        # Time complexity : O(N) since we go through the string of length N two times.
        # Space complexity : O(1) because English alphabet contains 26 letters.
            
        count = collections.Counter(s)
        
        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx
        
        return -1        