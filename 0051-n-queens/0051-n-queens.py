class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        visited = [-1]*n
        answer = []

        def is_okay(current_row):
            #1. 열이 겹치지 않는지, 대각선인지(행의 차이=열의 차이 같은 경우)
            for row in range(current_row):
                if visited[row] == visited[current_row] or current_row - row == abs(visited[current_row] - visited[row]):
                    return False
            return True

        def dfs(row):
            # 모든 행에 퀸이 놓였을 때
            if row == n:
                # .으로 된 grid 생성
                grid = [['.']*n for _ in range(n)]

                #visited에 담긴 좌표에만 Q찍어주기
                for index, num in enumerate(visited):
                    grid[index][num] = 'Q'

                result = []

                for row in grid:
                    result.append(''.join(row))

                answer.append(result)
                
                return

            # visited에 열 번호 넣기
            for col in range(n):
                visited[row]=col
                if is_okay(row):
                    dfs(row+1)


        dfs(0)
        return answer