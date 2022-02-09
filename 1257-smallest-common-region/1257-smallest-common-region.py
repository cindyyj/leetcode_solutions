class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        parents = {}
        for region in regions: # Build the parent dictionary, parents[child] -> parent 
            for i in range(1,len(region)): 
                parents[region[i]] = region[0]
                
        a = region1 #pointer for linkedlist 1
        b = region2 #pointer for linkedlist 2
        while a!=b: 
            # if the current node has parent, then go to its parent.
            # If the current node is the last one (e.g. Earth) then go to the other region retarting the process.
            a = parents[a] if a in parents else region2 
            b = parents[b] if b in parents else region1
        return a
        