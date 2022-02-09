class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        # https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank/solution/qian-zhui-he-si-xiang-yi-dao-shou-huo-he-veza/
        
        n = len(security)
        left = [0] * n  # 前面递增的个数
        right = [0] * n # 后面递减的个数
        
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                left[i] = left[i - 1] + 1
            # else left[i] = 0
        
        for i in range(n-2, -1, -1):
            if security[i + 1] >= security[i]:
                right[i] = right[i + 1] + 1
                
        ans = []
        for i in range(n):
            if left[i] >= time and right[i] >= time:
                ans.append(i)
        return ans
 