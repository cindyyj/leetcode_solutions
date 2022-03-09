class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        """
        immutable does not mean you can't reassign the variable, it means you cannot edit its content, by which I mean the below is ok :

        s = 'bla'
        s= 'blb'
        but this is not ok:

        s = 'bla'
        s[2] ='b'
        """
        
        nums = "".join([str(ord(ch) - ord('a') + 1) for ch in s])
        while k:
            nums = str(sum(list(map(int, nums))))            
            k -= 1
        
        return int(nums)            