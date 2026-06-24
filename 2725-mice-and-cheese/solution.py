class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        ans = sum(reward2)

        diff = []
        for a, b in zip(reward1, reward2):
            diff.append(a - b)

        diff.sort(reverse=True)

        for i in range(k):
            ans += diff[i]

        return ans
