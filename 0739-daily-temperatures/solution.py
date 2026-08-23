class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = len(temps) * [0]

        for i, temp in enumerate(temps):
            while stack and stack[-1][0] < temp:
                r_temp, r_ind = stack.pop()
                res[r_ind] = i - r_ind
            stack.append((temp, i))
        return res

        
