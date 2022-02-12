class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        total = 0
        
        # 不生气时间内的顾客总数
        for i in range(n):
            if grumpy[i] == 0:
                total += customers[i]
        
        # 在窗口 X 内因为生气而被赶走的顾客数
        angry = 0
        maxangry = 0
        start = 0
        for end in range(n):
            if grumpy[end] == 1:
                angry += customers[end]
            
            # keep sliding window size minutes
            if end >= minutes:
                if grumpy[start] == 1:
                    angry -= customers[start]
                start += 1
            
            maxangry = max(maxangry, angry)       
        
        return total + maxangry
        
        
        """
        所有不生气时间内的顾客总数：使用 i 遍历[0, customers.length)[0,customers.length)，累加grumpy[i] == 0时的customers[i]。
        在窗口 X 内因为生气而被赶走的顾客数：使用大小为 X 的滑动窗口，计算滑动窗口内的grumpy[i] == 1时的customers[i]，得到在滑动窗口内老板生气时对应的顾客数。

        作者：fuxuemingzhu
        链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner/solution/yong-mi-mi-ji-qiao-wan-liu-zhu-zui-duo-d-py41/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """