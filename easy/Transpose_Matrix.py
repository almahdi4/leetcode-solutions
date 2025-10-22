class Solution:
# 867. Transpose Matrix
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Approach: Iterate through columns and build each transposed row.
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transpose_matrix = []
        for col in range(len(matrix[0])):
            new_row = []
            for rows in range(len(matrix)):
                new_row.append(matrix[rows][col])
            transpose_matrix.append(new_row)

        return transpose_matrix
