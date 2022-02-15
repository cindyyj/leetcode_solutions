class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = ["0", "1", "8"] if n % 2 else [""]
        for i in range(n // 2)[::-1]:
            res = [s[0] + n + s[1] for s in ["00", "11", "88", "69", "96"][i == 0:] for n in res]
        return res     
    
    
    """
    a[n<2:]

# this one could mean a[True:] or a[False:]
I googled the syntax, but I couldn't find any reference related to it.
So, I experimented it.
a[True:] : this returns the subset, [1:]
a[False:] : this returns the subset, [0:]


    """