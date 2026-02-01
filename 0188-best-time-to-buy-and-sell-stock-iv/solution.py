class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        cash = [0] * (k + 1)
        hold = [-10**18] * (k + 1)

        for p in prices:
            for t in range(k):
                hold[t] = max(hold[t], cash[t] - p)
                cash[t + 1] = max(cash[t + 1], hold[t] + p) 

        return max(cash)








