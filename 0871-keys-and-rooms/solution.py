class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vv = set()
        def dfs(room):
            vv.add(room)
            for i in rooms[room]:
                if i not in vv:
                    dfs(i)           
        dfs(0)
        return len(vv) == len(rooms)
