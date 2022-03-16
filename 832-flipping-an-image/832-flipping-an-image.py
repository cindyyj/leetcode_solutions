class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        # reverse & flip
        res = []
        for row in image:
            row = row[::-1]
            res.append(list(map(lambda x : 0 if x == 1 else 1, row)))
        
        return res
        