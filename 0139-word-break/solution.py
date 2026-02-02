class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        maxLen = max(map(len, wordDict)) if wordDict else 0

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            start = max(0, i - maxLen)
            for j in range(start, i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]
