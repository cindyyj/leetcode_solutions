class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # number of odds in [1, low) is low //2
        # number of odds in [1, high] is (high + 1) //2
        
        return (high + 1) //2 - low //2
        