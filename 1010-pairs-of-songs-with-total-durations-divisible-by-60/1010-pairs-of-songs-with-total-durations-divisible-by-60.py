from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        # 因为模是60，所以哈希表的长度最多为60，空间复杂度可改成常数O(1)吧。
        # 还有不用预处理，可以一边处理一边统计，这样遍历一次就好
        
        d = defaultdict(int)
        
        res = 0
        for t in time:
            key = t % 60
            if key == 0:
                res += d[key]
            else:
                res += d[60-key]
            d[key] += 1
            
        return res
        
        
        # # brute force, TLE
        # t = [num % 60 for num in time]        
        # return sum([(i + j) % 60 == 0 for i, j in itertools.combinations(t, 2)])