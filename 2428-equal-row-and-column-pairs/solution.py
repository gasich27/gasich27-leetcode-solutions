class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = [tuple(grid[i]) for i in range(n)]

        cols = []
        for j in range(n):
            column = tuple(grid[i][j] for i in range(n))
            cols.append(column)

        count = 0
        for row in rows:
            for col in cols:
                if row == col:
                    count += 1
        
        return count
