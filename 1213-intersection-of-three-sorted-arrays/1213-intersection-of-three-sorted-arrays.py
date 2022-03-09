class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        # return sorted(set(arr1) & set(arr2) & set(arr3))
    
        return [k for k, v in Counter(arr1 + arr2 + arr3).items() if v == 3]