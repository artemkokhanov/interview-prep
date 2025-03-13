from typing import List


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = []
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)

    while left < right and top < bottom:
        # get every i in the top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # get every i in the right most column
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        # checking if our pointers are still within the bounds of each other
        # see what happens if we have a single row matrix for example ([[1, 2, 3]])
        # spoiler: the code will exit here correctly
        if not (left < right and top < bottom):
            break

        # get every i in the bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # get every i in the left most column
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res
