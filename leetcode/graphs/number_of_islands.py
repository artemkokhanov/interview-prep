from collections import deque
from typing import List


# runs in O(M * N) where M is the number of rows and N is the number of columns
# space complexity is O(M * N)
def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):
        queue = deque()
        visit.add((r, c))
        queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                if (r + dr) in range(rows) and (c + dc) in range(cols) and grid[r + dr][c + dc] == "1" and (
                        (r + dr, c + dc)) not in visit:
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands
