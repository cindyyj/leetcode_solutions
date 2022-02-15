class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)
        
        for i in range(n-1, -1, -1):
            if i + zeros < n:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0
        
        
"""
challenge: change in place 
Start from the back and adjust items to correct locations. If item is zero then duplicate it.

https://leetcode.com/problems/duplicate-zeros/discuss/322576/Python-3-real-in-place-solution
"""