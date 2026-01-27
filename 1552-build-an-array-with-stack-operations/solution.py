class Solution:
    def buildArray(self, target, n):
        res = []
        j = 0  # индекс в target

        for x in range(1, n + 1):
            if j == len(target):
                break

            res.append("Push")
            if x == target[j]:
                j += 1
            else:
                res.append("Pop")

        return res

