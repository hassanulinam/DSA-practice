# def searchMatrix(matrix: list[list[int]], target: int) -> bool:
#     m, n = len(matrix), len(matrix[0])

#     i, j = 0, n - 1

#     while i >= 0 and j >= 0 and i < m and j < n:
#         if matrix[i][j] == target:
#             return True
#         if matrix[i][j] > target:
#             j -= 1
#         else:
#             i += 1
#     return False
#
#
# ------
# Since given matrix is sorted as if a flat array, we can leverage Binary search, thereby decreasing time complexity
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    l = m * n

    left = 0
    right = l - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 60
print(searchMatrix(matrix, target))
