class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # d = defaultdict(list)
        # for piece in pieces:
        #     d[piece[0]] = piece
        d = {piece[0] : piece for piece in pieces}
        
        target = []
        for num in arr:
            # target += d[num]
            target += d.get(num, [])
        return target == arr