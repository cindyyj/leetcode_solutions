class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        
        # BFS, build from center 
        all_pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
        nonzero_pairs = all_pairs[1:]

        curr_level = ["0", "1", "8"] if n % 2 == 1 else [""]

        for level in range(0, n // 2):
            next_level = []
            for num in curr_level:
                pairs = all_pairs if len(num) < n - 2 else nonzero_pairs
                for left, right in pairs:
                    next_level.append(left + num + right)
            curr_level = next_level
            
        return curr_level
    
    
        # res = ["0", "1", "8"] if n % 2 else [""]
        # for i in range(n // 2)[::-1]:
        #     res = [s[0] + n + s[1] for s in ["00", "11", "88", "69", "96"][i == 0:] for n in res]
        # return res     
    
    
    """
    a[n<2:]

# this one could mean a[True:] or a[False:]
I googled the syntax, but I couldn't find any reference related to it.
So, I experimented it.
a[True:] : this returns the subset, [1:]
a[False:] : this returns the subset, [0:]
@GatsbyLee Yes, because bool is a subclass of int and False == 0 and True == 1.



    """