class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
        # ~, not, Inverts all the bits
        # helps us find the i-th value of the row, counting from the right.
        # Python’s Tilde ~n operator is the bitwise negation operator: it takes the number n as binary number and “flips” all bits 0 to 1 and 1 to 0 to obtain the complement binary number. For example, the tilde operation ~1 becomes 0 and ~0 becomes 1 and ~101 becomes 010.
        
        # The general formula to calculate the tilde operation ~i on an integer value i is ~i=-i-1.
        
        
#         # reverse & flip
#         res = []
#         for row in image:
#             row = row[::-1]
#             res.append(list(map(lambda x : 0 if x == 1 else 1, row)))
        
#         return res
        
        # in-place change!
        for row in image:
            for i in range((len(row) + 1) // 2):
                row[~i], row[i] = row[i]^1, row[~i]^1
                # row[len(row) - 1 - i], row[i] = row[i]^1, row[len(row) - 1 - i] ^ 1        
        return image