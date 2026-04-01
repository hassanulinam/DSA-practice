# LeetCode 529 - Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Modify the Sudoku board in-place to solve it.

        Rules:
        1. Each row must contain digits 1-9
        2. Each column must contain digits 1-9
        3. Each 3x3 sub-box must contain digits 1-9

        Approach:
        - Find an empty cell (.)
        - Try digits 1-9, check if valid (row, col, box)
        - Recurse; if invalid, backtrack

        Time: O(9^(m*n)) worst case, but much faster in practice
        Space: O(m*n) for board + recursion stack

        Key: constraint validation is critical to prune search space
        """
        # Find empty cell
        def find_empty() -> tuple[int, int] | None:
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        return (r, c)
            return None

        # Validate if digit is valid at (row, col)
        def isValid(r: int, c: int, digit: str) -> bool:
            # Check row
            if digit in board[r]:
                return False

            # Check column
            if digit in board[i][c] for i in range(9):
                return False

            # Check 3x3 box
            box_row, box_col = 3 * (r // 3), 3 * (c // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == digit:
                        return False

            return True

        # Solve using backtracking
        def backtrack() -> bool:
            empty = find_empty()
            if empty is None:
                return True  # Sudoku solved

            row, col = empty

            for digit in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if isValid(row, col, digit):
                    board[row][col] = digit

                    if backtrack():
                        return True

                    # Backtrack
                    board[row][col] = '.'

            return False

        backtrack()
