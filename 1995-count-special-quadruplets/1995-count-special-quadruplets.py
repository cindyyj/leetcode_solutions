class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/count-special-quadruplets/solution/tong-ji-te-shu-si-yuan-zu-by-leetcode-so-50e2/
        # walrus operator
        # b < c < d < n, c, d in [b + 1, n - 1]
        
        n = len(nums)
        ans = 0
        cnt = Counter()
        
        for c in range(n - 2, 0, -1):
            cnt[nums[c + 1]] += 1
            for a in range(c):
                for b in range(a + 1, c):
                    if (total := nums[a] + nums[b] + nums[c]) in cnt:
                        ans += cnt[total]
                        
        return ans