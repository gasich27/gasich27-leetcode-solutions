class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        know_char = set()
        left = 0

        for i, right_char in enumerate(s):
            while right_char in know_char:
                know_char.remove(s[left])
                left += 1
            know_char.add(right_char)
            result = max(result, i - left + 1)
        return result

