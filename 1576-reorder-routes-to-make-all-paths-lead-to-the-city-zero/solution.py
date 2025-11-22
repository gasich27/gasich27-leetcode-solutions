class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        
        def dfs(city, parent):
            changes = 0
            for neighbor, needs_reverse in graph[city]:
                if neighbor != parent:
                    changes += needs_reverse
                    changes += dfs(neighbor, city)
            return changes
        
        return dfs(0, -1)
