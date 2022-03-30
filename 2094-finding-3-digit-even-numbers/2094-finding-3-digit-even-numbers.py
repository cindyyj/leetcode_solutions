class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        # O(n)
        ans = []
        freq = Counter(digits)
        for num in range(100, 999, 2):
            if not (Counter(int(d) for d in str(num)) - freq):
                ans.append(num)
        return ans
             
        
        # ans = set()
        # for x, y, z in itertools.permutations(digits, 3):
        #     if x != 0 and z & 1 == 0:
        #         ans.add(100*x + 10*y + z)
        # return sorted(ans)
        
        