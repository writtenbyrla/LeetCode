class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        for row in range(len(matrix)):
            start, end = 0, len(matrix[0])-1

            while start <= end:
                mid = (start + end) // 2

                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    end = mid-1
                else:
                    start = mid +1

        return False 