class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = [0]
        if not operations:
            return 0

        for i in operations:
            if i == 'C':
                s.pop()
            elif i == '+':
                r = s[-1] + s[-2]
                s.append(r)
            elif i == 'D':
                v = s[-1] * 2
                s.append(v)
            else:
                s.append(int(i))
        
        return sum(s)


