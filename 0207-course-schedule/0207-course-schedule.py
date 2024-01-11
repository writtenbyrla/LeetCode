class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # numCourses: 총 들어야하는 수업 갯수(0부터 numCourses-1)
        # prerequisites: 선수과목 b1을 가려면 a1을 거쳐가야함
        # prerequisites[i] = [a, b]일 때 ai를 들으려면 bi를 들어야함 -> 뒤에 있는게 선수과목
        # 모든 수업 듣기 가능하면 true, 불가능하면 false

        visited = set() # 방문확인
        route = set() # 방문경로
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a) # 선행과목에 대한 딕셔너리

        def dfs(x):
            if x in route:
                return False
            if x in visited:
                return True

            visited.add(x)
            route.add(x)

            for arrive in graph[x]:
                if not dfs(arrive):
                    return False
            route.remove(x)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True