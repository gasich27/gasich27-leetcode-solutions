class Solution:
    def findCircleNum(self, graf: List[List[int]]) -> int:
        n = len(graf)
        visited = [False] * n
        provinces = 0
        
        def dfs(city):
            visited[city] = True
            for neighbor in range(n):
                if graf[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
        
        return provinces




