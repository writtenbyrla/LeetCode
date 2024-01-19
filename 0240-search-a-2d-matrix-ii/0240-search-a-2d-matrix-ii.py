class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row, col = 0, len(matrix[0])-1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            # target보다 큰 경우 더 작아야 하므로 왼쪽으로 이동
            elif matrix[row][col] > target:
                col -= 1
            # target보다 작은 경우 값이 더 커야하므로 아래로 이동
            else:
                row += 1
        return False