class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(r, c, size):
            first = grid[r][c]
            same = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(first == 1, True)

            half = size // 2

            return Node(
                False,
                False,
                dfs(r, c, half),                  
                dfs(r, c + half, half),            
                dfs(r + half, c, half),            
                dfs(r + half, c + half, half)      
            )

        return dfs(0, 0, len(grid))