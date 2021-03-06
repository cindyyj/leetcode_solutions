class SparseVector:
    def __init__(self, nums: List[int]):
        self.svec = defaultdict(int)
        self.svec = {i:v for i,v in enumerate(nums) if v} 
        
    def dotProduct(self, vec: 'SparseVector') -> int:
        res=0
        for i,v in self.svec.items():
            # dict.get(key, default = None)
            # key − This is the Key to be searched in the dictionary.
            # default − This is the Value to be returned in case key does not exist.
            res += v * vec.svec[i]

            # res+=v*vec.svec.get(i,0)  

        return res
    
    
#     # fb 
#     # efficient: store the non-zero values and their corresponding indices in a dictionary, with the index being the key 
    
#     def __init__(self, nums: list[int]):
#         self.nonzeros = {}
#         for i, n in enumerate(nums):
#             if n != 0:
#                 self.nonzeros[i] = n
                
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         res = 0
        
#         for i, n in self.nonzeros.items():
#             if i in vec.nonzeros:
#                 res += n * vec.nonzeros[i]
        
#         return res
            
    
    
    # inefficient, store a sparse vector as an array
    def __init__(self, nums: List[int]):
        self.array = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for num1, num2 in zip(self.array, vec.array):
            res += num1 * num2
        return res
            
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)