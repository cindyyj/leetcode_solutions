class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        d = defaultdict(int)
        cnt = 0
        
        for n1 in nums1:
            for n2 in nums2:
                d[n1 + n2] += 1
        
        for n3 in nums3:
            for n4 in nums4:
                if -(n3 + n4) in d:
                    cnt += d[-(n3 + n4)]
        
        return cnt
    
    """
    初始化哈希表。
    分组：nums1 和 nums2 一组，nums3 和 nums4 一组。
    分别对 nums1 和 nums2 进行遍历，将所有 nums1 和 nums2 的值的和作为哈希表的 key，和的次数作为哈希表的 value。

    作者：rocky0429-2
    链接：https://leetcode-cn.com/problems/4sum-ii/solution/acm-xuan-shou-tu-jie-leetcode-si-shu-xia-ocpe/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """