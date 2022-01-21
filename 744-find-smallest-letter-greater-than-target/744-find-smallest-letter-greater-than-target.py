class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # binary search, right boundary
        
        l, r = 0, len(letters)-1
        while l <= r:
            mid = l + (r-l) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        
        if r < 0 or l >= len(letters):
            return letters[0]
        else:
            return letters[l]
            
        # # https://leetcode.com/problems/find-smallest-letter-greater-than-target/solution/
        # for c in letters:
        #     if c > target:
        #         return c
        # return letters[0]
        