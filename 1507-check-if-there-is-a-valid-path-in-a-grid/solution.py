class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True

        # Map each street type to its possible movement directions (dr, dc)
        street_dirs = {
            1: [(0, -1), (0, 1)],   # left, right
            2: [(-1, 0), (1, 0)],   # up, down
            3: [(0, -1), (1, 0)],   # left, down
            4: [(0, 1), (1, 0)],    # right, down
            5: [(0, -1), (-1, 0)],  # left, up
            6: [(0, 1), (-1, 0)]    # right, up
        }

        # Map each movement direction to the set of street types that can accept entry from that direction
        valid_incoming = {
            (1, 0): {2, 5, 6},   # moving down -> entering neighbor from top
            (-1, 0): {2, 3, 4},  # moving up -> entering neighbor from bottom
            (0, 1): {1, 3, 5},   # moving right -> entering neighbor from left
            (0, -1): {1, 4, 6}   # moving left -> entering neighbor from right
        }

        queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True

            # Try all directions allowed by the current street type
            for dr, dc in street_dirs[grid[r][c]]:
                nr, nc = r + dr, c + dc
                # Check bounds, visited status, and street compatibility
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if grid[nr][nc] in valid_incoming[(dr, dc)]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        return False
