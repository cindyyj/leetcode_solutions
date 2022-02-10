class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按照h维度的身高顺序从高到低排序。确定第一个维度
        # lambda返回的是一个元组：当-x[0](维度h）相同时，再根据x[1]（维度k）从小到大排序

        # 作者：carlsun-2
        # 链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/406du-shuo-shi-tan-xin-na-yao-wei-shi-yao-yong-tan/
        # Sort people:
        # - In the descending order by height.
        # - Among the guys of the same height, in the ascending order by k-values.
        # Take guys one by one, and place them in the output array at the indexes equal to their k-values.
        # Return output array.
        
        people.sort(key=lambda x : (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
    
        """
        People are only counting (in their k-value) taller or equal-height others standing in front of them. So a smallest person is completely irrelevant for all taller ones. And of all smallest people, the one standing most in the back is even completely irrelevant for everybody else. Nobody is counting that person. So we can first arrange everybody else, ignoring that one person. And then just insert that person appropriately. Now note that while this person is irrelevant for everybody else, everybody else is relevant for this person - this person counts exactly everybody in front of them. So their count-value tells you exactly the index they must be standing.

        So you can first solve the sub-problem with all but that one person and then just insert that person appropriately. And you can solve that sub-problem the same way, first solving the sub-sub-problem with all but the last-smallest person of the subproblem. And so on. The base case is when you have the sub-...-sub-problem of zero people. You're then inserting the people in the reverse order, i.e., that overall last-smallest person in the very end and thus the first-tallest person in the very beginning. That's what the above solution does, Sorting the people from the first-tallest to the last-smallest, and inserting them one by one as appropriate.
        """