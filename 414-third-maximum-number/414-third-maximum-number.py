class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 时间复杂度：使用 Set 去重的复杂度为 O(n)；排序复杂度为 O(nlogn)。整体复杂度为 O(nlogn)
        # 空间复杂度：O(n)
        
        n = sorted(set(nums))
        if not n:
            return None        
        if len(n) >= 3:
            return n[-3]
        else:
            return n[-1]