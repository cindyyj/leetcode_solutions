class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # Create a set containing the integers from 1...n then check that each set of rows and columns is equal to this set.
        # zip(*matrix) is a convenient way of obtaining the columns of a matrix
        # set is unordered!!!
        target = [num for num in range(1, len(matrix) + 1)]   
        return all(set(target) == set(x) for x in matrix + list(zip(*matrix)))
        