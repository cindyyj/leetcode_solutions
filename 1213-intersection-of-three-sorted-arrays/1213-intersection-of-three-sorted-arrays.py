class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        # 3-pointers
        
        i = j = k = 0
        res = []
        
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
                continue
            
            largest = max(arr1[i], arr2[j], arr3[k])
            if arr1[i] < largest:
                i += 1
            if arr2[j] < largest:
                j += 1
            if arr3[k] < largest:
                k += 1
            
        return res
        
        
        # return sorted(set(arr1) & set(arr2) & set(arr3))
        # return [k for k, v in Counter(arr1 + arr2 + arr3).items() if v == 3]