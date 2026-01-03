class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        leteri = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        path = []

        def comb(i: int):
            if i == len(digits):
                res.append("".join(path))
                return
            
            letters = leteri[digits[i]]
            for ch in letters:
                path.append(ch)
                comb(i + 1)
                path.pop()

        comb(0)
        return res

