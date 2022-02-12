class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d ={r: list1.index(r) + list2.index(r) for r in set(list1) & set(list2)}
        return [r for r in d if d[r] == min(d.values())]
        
        # time O(l1+l2), space(min(l1,l2)* x); x average string length
        
        if (len(list1) > len(list2)):
            return self.findRestaurant(list2, list1)
        
        # restaurant:i
        dict1 = {r : i for i, r in enumerate(list1)}
        dict2 = {r: dict1[r] + i for i, r in enumerate(list2) if r in dict1}
        
        MIN = float('inf')
        res = []
        
        for key, val in dict2.items():
            if val < MIN:
                res = [key]
                MIN = val
            elif val == MIN:
                res.append(key)
                
        return res
        
        
        # 2 line solution
        d = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
        return [x for x in d if d[x] == min(d.values())]
        