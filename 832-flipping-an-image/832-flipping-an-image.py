class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
        # ~, not, Inverts all the bits
        # helps us find the i-th value of the row, counting from the right.
        
#         # reverse & flip
#         res = []
#         for row in image:
#             row = row[::-1]
#             res.append(list(map(lambda x : 0 if x == 1 else 1, row)))
        
#         return res
        
        # in-place change!
        for row in image:
            for i in range((len(row) + 1) // 2):
                row[len(row) - 1 - i], row[i] = row[i]^1, row[len(row) - 1 - i] ^ 1        
        return image