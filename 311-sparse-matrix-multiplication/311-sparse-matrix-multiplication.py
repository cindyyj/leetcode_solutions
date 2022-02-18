class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        n, m, k = len(A), len(B[0]), len(A[0])
        C = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for t in range(k):
                    C[i][j] += A[i][t] * B[t][j]
        return C         