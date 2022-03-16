class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key= lambda x: -x[1])
        
        i = units = 0
        while truckSize > 0 and i < len(boxTypes):
            boxes = min(truckSize, boxTypes[i][0])
            units += boxes * boxTypes[i][1] 
            truckSize -= boxes
            i += 1
        
        return units