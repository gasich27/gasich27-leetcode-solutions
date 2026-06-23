class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        groups = 0
        used = 0

        while used + groups + 1 <= n:
            groups += 1
            used += groups

        return groups
