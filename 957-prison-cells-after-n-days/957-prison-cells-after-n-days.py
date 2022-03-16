class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # game of life
        # give K cells, at most 2**k possible states
        # if steps > number of all possible states, repeat sooner or later
        
        # cells.length == 8
        k = 8
        def nextday(cells):
            return [int(i > 0 and i < k-1 and cells[i-1] == cells[i+1])
                    for i in range(k)]

        # find the loop!!!
        seen = defaultdict(int)
        for i in range(n):
            state = tuple(cells)
            if state in seen:
                loop_len = i - seen[state]
                return self.prisonAfterNDays(cells, (n - i) % loop_len)
            else:
                seen[state] = i
                cells = nextday(cells)
        return cells