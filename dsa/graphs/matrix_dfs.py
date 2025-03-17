# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]


# Count paths (backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
            r == ROWS or c == COLS or
            (r, c) in visit or
            grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0  # count keeps track of how many different ways we can reach the result from the current location
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r - 1, c + 1, visit)
    count += dfs(grid, r - 1, c - 1, visit)

    visit.remove((r, c))
    return count  # we return the count to the previous node/vertex which will return its count to its previous node/vertex, etc.


print(dfs(grid, 0, 0, set()))
