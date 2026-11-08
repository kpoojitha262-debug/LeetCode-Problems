class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        row_count = [0] * rows
        col_count = [0] * cols
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        communicating_servers = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if row_count[r] > 1 or col_count[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers