class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x:-x[1])
        units = i = 0
        
        while truckSize > 0 and i < len(boxTypes):
            cnt = min(truckSize, boxTypes[i][0])
            units += cnt * boxTypes[i][1]
            truckSize -= cnt
            i += 1
        
        return units