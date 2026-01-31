class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapST = {}
        mapTS = {}

        for cs, ct in zip(s, t):
            if cs in mapST and mapST[cs] != ct:
                return False
            if ct in mapTS and mapTS[ct] != cs:
                return False

            mapST[cs] = ct
            mapTS[ct] = cs

        return True
