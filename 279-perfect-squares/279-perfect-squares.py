class Solution:
    def numSquares(self, n: int) -> int:
        
        q = collections.deque([(n,0)])
        seen = set()
        
        step = 0
        while q:
            num, step = q.popleft()
            targets = [num - i*i for i in range(1, int(num**0.5) + 1)]
            for target in targets:
                if target == 0:
                    return step + 1
                if target not in seen:
                    q.append((target, step + 1))
                    seen.add(target)
        
        return 0